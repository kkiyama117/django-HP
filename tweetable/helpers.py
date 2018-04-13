#!/usr/bin/env python
# -*- coding: utf-8 -*-
from environ import environ
from requests_oauthlib import OAuth1Session



CK = '6aVCqjTroUzYmFlZfj830EjJY'  # Consumer Key
CS = 'f52IftXxjbBIXHswa78MfAFZghg5mG99VIGHbLvAGgn8b8vAfO'  # Consumer Secret
AT = '3246502376-51mC9RtUKr7F0hcLqFSUrlaTflfSn8mmzFddl6v'  # Access Token
AS = 'jnpqnAEU4QzZ7yZ7aswjRPmtgO5mIqsWnKLbzeIE8xjuP'  # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "Hello, World!"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params=params)

# レスポンスを確認
if req.status_code == 200:
    print("OK")
else:
    print("Error: %d" % req.status_code)
