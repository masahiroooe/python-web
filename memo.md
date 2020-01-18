# Python Web Server memo

```
python3 -m http.server 8000
python3 -m http.server --cgi 8000
```

```
# https://stackoverflow.com/a/41366949/531320
openssl req -x509 -newkey rsa:4096 -sha256 \
-nodes -keyout server.key -out server.crt \
-subj "/CN=example.com" -days 3650
```