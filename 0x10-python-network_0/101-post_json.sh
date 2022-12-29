#!/bin/bash
# script sends a JSON POST request to a URL and displays the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
