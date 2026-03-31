#!/bin/bash

# Usage: ./escape.sh <directory> [log_file]

TARGET_DIR=$1
LOG_FILE=$2

if [ -z "$TARGET_DIR" ]; then
    echo "Usage: $0 <directory> [log_file]"
    exit 1
fi

find "$TARGET_DIR" -type f ! -name "$LOG_FILE" ! -name "$(basename "$0")" | while read -r file; do
    # delete all instances of {target="_blank"}
    sed -i 's/{target="_blank"}//g' "$file"

    # escape all {} in directory files & log
    if [ ! -z "$LOG_FILE" ]; then
        grep -o "[^{]{[^}]*}" "$file" | sed "s|^|$file: |" >> "$LOG_FILE"
    fi

    sed -i 's/{\([^}]*\)}/{{\1}}/g' "$file"
done

[[ ! -z "$LOG_FILE" ]] && echo "Logs saved to: $LOG_FILE"
