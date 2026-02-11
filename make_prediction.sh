#!/bin/bash

URL=$1

curl -X POST "$URL/predict" \
     -H "Content-Type: application/json" \
     -d '{"features":[1,2,3,4]}'