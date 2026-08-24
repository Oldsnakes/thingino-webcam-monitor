#!/bin/sh
# BusyBox httpd CGI for JSON API
# Expects request body (application/json)

echo "Content-Type: application/json"
echo $1 
echo $QUERY_STRING 
echo $QUERY_STRING >&2

prudyntctl json $QUERY_STRING

# Read exactly CONTENT_LENGTH bytes if provided; otherwise read all stdin
# if [ -n "$CONTENT_LENGTH" ]; then
#	dd bs=1 count="$CONTENT_LENGTH" 2>/dev/null | prudyntctl json -
#else
#	prudyntctl json -
#fi

