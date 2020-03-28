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

```
git remote add origin https://github.com/masahiroooe/python-web.git
git pull https://github.com/masahiroooe/python-web.git master
git merge --allow-unrelated-histories origin/master

```

```
# The version of Anaconda may be different depending on when you are installing`
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
sh Miniconda3-latest-MacOSX-x86_64.sh
# and follow the prompts. The defaults are generally good.`
```
