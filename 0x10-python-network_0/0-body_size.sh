#!/bin/bash
# script takes in URL, sends request to it and displays size of response body
curl -s "$1" | wc -c
