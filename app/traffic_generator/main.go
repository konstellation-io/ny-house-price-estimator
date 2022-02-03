package main

import (
	"fmt"
	"log"
	"sync"
	"time"

	vegeta "github.com/tsenart/vegeta/lib"
)

var AppUrl string = "https://demo.kre-demo.konstellation.io/api/"
var ReportPredictionAccuracy int = 70
var testDuration time.Duration = 20 * time.Minute

const (
	Reset string = "\033[0m"
	Red   string = "\033[31m"
	Green string = "\033[32m"
)

var wg sync.WaitGroup

func vegetaAttack(rate vegeta.Pacer, duration time.Duration, targeter vegeta.Targeter, color string) {
	attacker := vegeta.NewAttacker()
	var metrics vegeta.Metrics
	for res := range attacker.Attack(targeter, rate, duration, "Load Test") {
		if res.Error != "" {
			log.Println(color + res.Error + Reset)
		}

		metrics.Add(res)
	}
	metrics.Close()
	fmt.Printf("%+v  \n", metrics)
}

func makePrediction() {
	rate := vegeta.Rate{Freq: 1, Per: 2 * time.Second}
	targeter := SavePredictionTarget(Red)
	vegetaAttack(rate, testDuration, targeter, Red)
	wg.Done()
}

func savePrediction() {
	rate := vegeta.Rate{Freq: 1, Per: 2 * time.Second}
	targeter := MakePredictionTarget(Green)
	vegetaAttack(rate, testDuration, targeter, Green)
	wg.Done()
}

func main() {
	wg.Add(2)
	go makePrediction()
	go savePrediction()

	wg.Wait()
}
