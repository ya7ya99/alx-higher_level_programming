#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL provided as the first argument
url=$1

# Sending a GET request with curl
# -H option is used to specify the header variable
# -s option is used for silent mode (to suppress progress meter)
# -o option is used to output the response body to stdout
# -w option is used to display only the response body
# -X option specifies the HTTP method (GET by default)
# --header option is used to specify the header
response=$(curl -s -X GET "$url" -H "X-School-User-Id: 98")

# Displaying the body of the response
echo "$response"

