#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from django.core.exceptions import ValidationError

from transfacils.factories import RouteFactory, StationFactory, TrainFactory, \
    PreviousStationFactory
from transfacils.models import Train, Route, Station


class RouteTest:
    def test_field_with_no_error(self):
        route = RouteFactory.build()
        try:
            route.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)

    def test_add_routes(self):
        before_route_count = Route.objects.all().count()
        RouteFactory.create()
        assert Route.objects.all().count() == before_route_count + 1


class StationTest:
    def setup(self):
        self.route = RouteFactory()
        self.previous_station = PreviousStationFactory(route=self.route)

    def test_field_with_no_error(self):
        station = StationFactory.build(route=self.route,
                                       previous_station=self.previous_station)
        try:
            station.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)

    def test_add_stations(self):
        before_station_count = Station.objects.all().count()
        StationFactory.create(route=self.route,
                              previous_station=self.previous_station)
        assert Station.objects.all().count() == before_station_count + 1


class TrainTest:
    @pytest.mark.django_db
    def setup(self):
        self.route = RouteFactory()

    @pytest.mark.django_db
    def test_field_with_no_error(self):
        train = TrainFactory.build(route=self.route)
        try:
            train.full_clean()
        except ValidationError as e:
            pytest.fail()
            print(e)

    @pytest.mark.django_db
    def test_add_trains(self):
        before_train_count = Train.objects.all().count()
        train = TrainFactory.create(route=self.route)
        assert Train.objects.all().count() == before_train_count + 1
