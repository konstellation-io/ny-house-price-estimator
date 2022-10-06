package main

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/golang/protobuf/jsonpb"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

var basicAuth string = os.Getenv("BASIC_AUTH_CREDENTIALS")

func proxyMakePrediction(w http.ResponseWriter, req *http.Request) {
	setupResponse(&w, req)
	if (*req).Method == "OPTIONS" {
		return
	}

	grpcReq := &Request{}

	switch req.Method {
	case "POST":
		err := jsonpb.Unmarshal(req.Body, grpcReq)
		if err != nil {
			err := fmt.Errorf("error Invalid Request Body: %w", err)
			sendErrorResponse(w, err, http.StatusBadRequest)
			return
		}

		if grpcReq.GetNeighbourhood() == "" {
			fmt.Println("error Calling MakePrediction without Neighbourhood field")
			http.Error(w, "error Invalid Request Body", http.StatusBadRequest)

			return
		}

		fmt.Println("Body GRPC: ", grpcReq.String())
		fmt.Printf("Body GRPC Type: %#v", grpcReq)
	default:
		sendErrorResponse(w, errors.New("error Only POST Method"), http.StatusInternalServerError)
		return
	}

	log.Println("--------------  Calling MakePrediction Service -------------")

	cc, err := grpc.Dial(config.Entrypoint, grpc.WithTransportCredentials(credentials.NewTLS(&tlsConf)))
	if err != nil {
		err := fmt.Errorf("error calling service: %w", err)
		sendErrorResponse(w, err, http.StatusInternalServerError)
		return
	}
	defer cc.Close()

	c := NewEntrypointClient(cc)

	res, err := c.MakePrediction(context.Background(), grpcReq)
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

	js, err := json.Marshal(res)
	if err != nil {
		err := fmt.Errorf("error: Unmashall response: %w", err)
		sendErrorResponse(w, err, http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Authorization", "Basic" + basicAuth)
	w.Write(js)
}
