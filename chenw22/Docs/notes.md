2/13/2026
The current directory structure for roq differs from the one used by mkdocs - Test if there would be an effect by running mkdoc files through roq’s static site generator
Need to check if Mkdoc custom markdown commands work
Code snippet may need  <pre> </pre> to work or <pre>{@code}</pre>
2/20/2026
Got Quarkus environment running to test RoQ on personal device. Have to move files to fit directory structure of RoQ from mkdocs. Will work on it until it can run on RoQ
3/10/2026
Currently looking into how to minimally alter the files in order to get to RoQ format. Pages for mkdocs should be converatble to posts in content folder in Roq. Layout creation may be necessary.
4/21/2026 (Condensed Notes Of total process)
-- YAML file requires modifications (Openrewrite possible)
-- Shell code for creating and moving files for simplicity
-- Python (possibly can be repalced with Java for more unified framework) for reading through YAML and modifying filenames and content for more general version of migration.
-- Python also makes frontmatter in each md but may not be needed.
-- Openrewrite is possible as there is a way to modify text files directly. However, there is currently none for markdown specifically. Though the YAML file can be manioulated through openrewrite for future reference.
