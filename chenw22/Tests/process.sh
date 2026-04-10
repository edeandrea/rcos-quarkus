mkdir -p content
mkdir -p data
mkdir -p public

shopt -s dotglob nullglob
for item in * .*; do
  

  [[ "$item" == "content" || "$item" == "public" || "$item" == "data" || "$item" == "$(basename "$0")" ]] && continue

  if [[ "$item" == "images" || "$item" == "diagrams"]]; then
    mv -n "$item" public/
  else
    mv -n "$item" content/
  fi
done

shopt -u dotglob nullglob