#!/bin/bash

protoc -I=./ \
  --python_out=src/etl \
  --python_out=src/model \
  --python_out=src/output \
  --python_out=src/save-prediction-metric \
  --mypy_out=src/etl \
  --mypy_out=src/model \
  --mypy_out=src/output \
  --mypy_out=src/save-prediction-metric \
  ./*.proto

echo "Done"
