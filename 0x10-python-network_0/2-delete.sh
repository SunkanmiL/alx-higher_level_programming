#!/bin/bash
# script takes in URL, sends a DELETE request to it and displays response body
curl -sX DELETE "$1"
