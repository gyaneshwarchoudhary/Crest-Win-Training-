#!/bin/sh

curl -v -G -L "https://www.google.com/search" --data-urlencode "q=how to curl" | jq '.'
curl -v  "https://www.google.com/search"  | jq '.'
