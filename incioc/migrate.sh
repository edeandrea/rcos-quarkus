# Usage: ./escape.sh <log_file> 

LOG_FILE=$1
REPO_NAME="TESTING-L4J-SCRIPT"
DOCS_DIR="roq-docs"

### get code locally
### THIS IS FOR TESTING ONLY
echo "Cloning..."
git clone git@github.com:quarkusio/quarkus-workshop-langchain4j.git $REPO_NAME
cd $REPO_NAME
quarkus create app $DOCS_DIR -x=io.quarkiverse.roq:quarkus-roq
cd $DOCS_DIR 
quarkus ext add quarkus-roq

# debug
pwd
ls

### The following instructions are *specifically* for
#   migrating the lang4j workshop files.
#
### TODO: Possibly integrate w/Openrewrite?
echo "Copying content..."
mkdir content/ && mkdir content/old
mkdir public && mkdir public/images
# mkdir content/old && mv content/index.html content/old/
# mv posts/ content/old/
cp ../docs/docs/index.md content/
### TODO: `section-1` and `section-2` should be generalized; 
cp -r ../docs/docs/section-1 content/ 
cp -r ../docs/docs/section-2 content/ 
cp ../docs/docs/requirements.md content/
cp ../docs/docs/images/* public/images
echo "Finished copying content"

TARGET_DIR="content"

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
