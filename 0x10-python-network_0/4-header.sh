#!/bin/bash
# script takes in URL, sends a GET request to the URL & displays response body
curl -sH "X-School-User-Id: 98" "$1"
