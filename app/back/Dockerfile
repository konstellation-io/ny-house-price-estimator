FROM golang:1.14.12-alpine3.12 as builder
LABEL maintainer="Intelygenz - Konstellation Team"

WORKDIR /app

COPY go.* ./

RUN go mod download

COPY . .
RUN go build -o proxy .
RUN mkdir -p /var/log/app

CMD ["sh","-c","/app/proxy  2>&1 | tee -a /var/log/app/app.log"]
