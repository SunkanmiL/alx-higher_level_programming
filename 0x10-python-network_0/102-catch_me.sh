#!/bin/bash
# script makes a request to 0.0.0.0:5000/catch_me and recieves a message
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
