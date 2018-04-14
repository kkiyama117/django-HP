#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import time

from lib import utils

from tweetable.helpers import *

class FunctionsTest:

    @pytest.mark.tweetable
    def get_tweet_api_test(self):
        time.sleep(0.1)
        api=get_tweet_api()
        assert api.id == 984949286273073152
