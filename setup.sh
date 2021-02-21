mkdir -p ~/.streamlit/
echo "[general]
email = \"dme43@mail.aub.edu\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
