#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

import twitter

from lib import utils


class REST(Enum):
    GET = "GET"
    POST = "POST"


class KIND(Enum):
    TWEETS = "statues"
    POST = "post"


def get_tweet_api():
    # TODO 外部依存しない方式を取る.
    env = utils.env_file_setting()
    ck = env("TWITTER_CK")  # Consumer Key
    cs = env("TWITTER_CS")  # Consumer Secret
    at = env("TWITTER_AT")  # Access Token
    ats = env("TWITTER_AS")  # Accesss Token Secert
    api = twitter.Api(consumer_key=ck,
                      consumer_secret=cs,
                      access_token_key=at,
                      access_token_secret=ats,
                      input_encoding="utf-8")

    return api


def get_tweet():
    # ツイート本文
    api = get_tweet_api()
    statues = api.GetUserTimeline(api.VerifyCredentials().id, count=20)
    for s in statues:
        print(s.text)


if __name__ == '__main__':
    user2 = get_tweet_api().VerifyCredentials().AsDict()
    for a, b in user2.items():
        print(a, b)
