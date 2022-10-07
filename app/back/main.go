package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
	"os"
)

const defaultPort = "4000"
const bauth basicAuth = basicAuth{username: os.Getenv("USERNAME"), password: os.Getenv("PASSWORD")}

var tlsConf tls.Config

var config struct {
	Port       string
	Domain     string
	Entrypoint string
}

func main() {
	config.Domain = os.Getenv("DOMAIN_NAME")
	if config.Domain == "" {
		log.Fatalln("DOMAIN_NAME env var not defined")
	}

	config.Entrypoint = fmt.Sprintf("demo-entrypoint.%s:443", config.Domain)

	fmt.Println("*************----------ENTRYPOINT: ", config.Entrypoint)
	port := os.Getenv("PORT")
	if port != "" {
		config.Port = port
	} else {
		config.Port = defaultPort
	}

	tlsConf.InsecureSkipVerify = true

	http.HandleFunc("/api/make-prediction", proxyMakePrediction)
	http.HandleFunc("/api/save-metrics", proxySaveMetrics)

	fmt.Printf("Listening on port %s\n", config.Port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", config.Port), nil))
}

func sendErrorResponse(w http.ResponseWriter, err error, statusError int) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Println(err.Error())
	http.Error(w, err.Error(), statusError)
}

func setupResponse(w *http.ResponseWriter, _ *http.Request) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
	(*w).Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
	(*w).Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")
}
