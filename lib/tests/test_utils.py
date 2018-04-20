#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import time

from lib import utils


class FunctionsTest:

    @pytest.mark.system
    def get_data_from_env_test(self):
        time.sleep(0.1)
        env = utils.get_data_from_env("data_for_test")
        assert env("test_for_get_function") == "test"

    @pytest.mark.system
    def test_env_file_setting(self):
        time.sleep(0.1)
        env = utils.env_file_setting()
        assert env.bool("value_for_test")
