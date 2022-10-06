package main

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

func proxySaveMetrics(w http.ResponseWriter, req *http.Request) {
	setupResponse(&w, req)
	if (*req).Method == "OPTIONS" {
		return
	}

	var reqList []*SaveMetricRequest

	switch req.Method {

	default:
		sendErrorResponse(w, errors.New("error Only POST Method"), http.StatusInternalServerError)

		return

	case "POST":
		err := json.NewDecoder(req.Body).Decode(&reqList)
		if err != nil {
			err := fmt.Errorf("error Invalid Request Body: %w", err)
			sendErrorResponse(w, err, http.StatusBadRequest)

			return
		}

		log.Println("--------------  Calling SavePredictionMetric Service -------------")

		cc, err := grpc.Dial(config.Entrypoint, grpc.WithTransportCredentials(credentials.NewTLS(&tlsConf)),
			grpc.WithPerRPCCredentials(bauth))
		if err != nil {
			err := fmt.Errorf("error calling service: %w", err)
			sendErrorResponse(w, err, http.StatusInternalServerError)
			return
		}
		defer cc.Close()

		c := NewEntrypointClient(cc)

		for _, grpcReq := range reqList {
			if grpcReq.GetPredictedCategory() == "" {
				fmt.Printf("missing predicted-category field. skipping row: %#v\n", grpcReq)

				continue
			}

			if grpcReq.GetRealCategory() == "" {
				fmt.Printf("missing real-category field. skipping row: %#v\n", grpcReq)

				continue
			}

			if grpcReq.GetDate() < 0 {
				fmt.Printf("missing date field. skipping row: %#v\n", grpcReq)

				continue
			}

			fmt.Println("Body GRPC: ", grpcReq.String())
			fmt.Printf("Body GRPC Type: %#v", grpcReq)
			res, err := c.SavePredictionMetric(context.Background(), grpcReq)
			if err != nil {
				err := fmt.Errorf("error calling RuntimeRPC: %w", err)
				sendErrorResponse(w, err, http.StatusInternalServerError)
				return
			}

			if !res.Success {
				err := fmt.Errorf("error internal app: %w", err)
				sendErrorResponse(w, err, http.StatusInternalServerError)
				return
			}

			log.Printf("Response from server: %s", res.String())
		}
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNoContent)
}
