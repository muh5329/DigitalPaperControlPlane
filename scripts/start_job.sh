#!/bin/bash

# Check if an argument is provided
# if [ $# -eq 0 ]; then
#     echo "Usage: $0 <argument>"
#     exit 1
# fi
# nohup start_job.sh > output.log 2>&1 &

argument="$1"

while true; do
    ## run while connected
    python3 renderRandom.py 
    sleep 5
done