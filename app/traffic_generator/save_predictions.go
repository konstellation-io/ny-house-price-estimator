package main

import (
	"encoding/json"
	"log"
	"math/rand"
	"time"

	vegeta "github.com/tsenart/vegeta/lib"
)

type Prediction struct {
	Date              int64  `json:"date"`
	PredictedCategory string `json:"predicted_category"`
	RealCategory      string `json:"real_category"`
}

func SavePredictionTarget(color string) vegeta.Targeter {
	return func(tgt *vegeta.Target) error {
		if tgt == nil {
			return vegeta.ErrNilTarget
		}

		rand.Seed(time.Now().Unix())

		tgt.Method = "POST"

		tgt.URL = AppUrl + "save-metrics"

		cat := make([]string, 0)
		cat = append(cat, "low", "high", "lux")

		p := rand.Int() % len(cat)

		var r int
		if rand.Intn(100) < ReportPredictionAccuracy {
			r = p
		} else {
			r = rand.Int() % len(cat)
		}

		pred := Prediction{
			Date:              time.Now().Unix(),
			PredictedCategory: cat[p],
			RealCategory:      cat[r],
		}

		var payloads []Prediction
		payloads = append(payloads, pred)

		body, _ := json.Marshal(payloads)
		log.Println(color + string(body) + Reset)
		tgt.Body = []byte(body)
		return nil
	}
}
