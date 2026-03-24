```sh
### get code locally
git clone git@github.com:quarkusio/quarkus-workshop-langchain4j.git roq-test-l4j
cd roq-test-l4j
quarkus create app roq-docs -x=io.quarkiverse.roq:quarkus-roq
cd roq-docs/
quarkus ext add quarkus-roq

### The following instructions are *specifically* for
#   migrating the lang4j workshop files.
mkdir content/old && mv index.html content/old/
cp ../docs/docs/index.md content/
mv posts/ old/
cp -r ../docs/docs/section-1 .
cp -r ../docs/docs/section-2 .

#TODO: Replace all "{}" with "{{}}" to escape
```
