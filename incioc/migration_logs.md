```sh
### REPO NAME
REPO_NAME = "TESTING-L4J-SCRIPT"

### get code locally
git clone git@github.com:quarkusio/quarkus-workshop-langchain4j.git $REPO_NAME
cd $REPO_NAME
quarkus create app roq-docs -x=io.quarkiverse.roq:quarkus-roq
cd roq-docs/
quarkus ext add quarkus-roq

### The following instructions are *specifically* for
#   migrating the lang4j workshop files.
#
### TODO: Possibly integrate w/Openrewrite?
mkdir content/old && mv content/index.html content/old/
cp ../docs/docs/index.md content/
mv posts/ old/
### TODO: `section-1` and `section-2` should be generalized; 
cp -r ../docs/docs/section-1 content/ 
cp -r ../docs/docs/section-2 content/ 
cp ../docs/docs/requirements.md content/

# TODO: chmod + run script

cp ../docs/docs/images/* public/images
```
