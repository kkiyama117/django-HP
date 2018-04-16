#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import time

from transfacils.models import Train, Route


class RouteTest:
    def test_fields(self):
        pass

    def test_add_routes(self):
        assert Route.objects.all().count() == 1
