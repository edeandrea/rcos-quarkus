mkdir content
mkdir data
mkdir public

for item in * .*; do
  [[ "$item" == "." || "$item" == ".." ]] && continue

  [[ "$item" == "content" || "$item" == "public" ]] && continue

  if [[ "$item" == "images" || "$item" == "diagrams" ]]; then
    mv "$item" public/
  else
    mv "$item" content/
  fi
done