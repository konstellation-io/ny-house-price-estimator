package main

import (
	"encoding/json"
	"log"
	"math/rand"
	"strconv"

	vegeta "github.com/tsenart/vegeta/lib"
)

func randInt(min, max int) string {
	r := min + rand.Intn(max-min)
	return strconv.Itoa(r)
}

func MakePredictionTarget(color string) vegeta.Targeter {
	return func(tgt *vegeta.Target) error {
		if tgt == nil {
			return vegeta.ErrNilTarget
		}

		tgt.Method = "POST"

		tgt.URL = AppUrl + "make-prediction"

		payload := map[string]string{
			"bedrooms":      randInt(1, 6),
			"beds":          randInt(1, 7),
			"accommodates":  randInt(1, 5),
			"bathrooms":     randInt(1, 3),
			"room_type":     "Shared room",
			"neighbourhood": "Bronx",
			"latitude":      "40.791269430732555",
			"longitude":     "-73.96330053394196",
			"tv":            randInt(0, 2),
			"elevator":      randInt(0, 2),
			"internet":      randInt(0, 2),
		}
		body, _ := json.Marshal(payload)
		log.Println(color + string(body) + Reset)
		tgt.Body = []byte(body)
		return nil
	}
}
