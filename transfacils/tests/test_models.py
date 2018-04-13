#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import time


class TestModel:
    @pytest.mark.small
    def test_1(self):
        time.sleep(0.1)
        assert "aaa" == "aaa"

    @pytest.mark.small
    def test_2(self):
        time.sleep(0.1)
        assert "bbb" == "bbb"

    @pytest.mark.large
    def test_3(self):
        time.sleep(10)
        assert "a" == "a"
