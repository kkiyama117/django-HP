from datetime import datetime

import factory
import faker

from transfacils import models


class RouteFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Route

    name = "京阪本線"
    kind = "TRAIN"
    cd = 33001


class PreviousStationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Station

    name = "神宮丸太町"
    route = factory.SubFactory(RouteFactory)
    cd = 3300141
    group_cd = 3300141


class StationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Station

    name = "出町柳"
    route = factory.SubFactory(RouteFactory)
    cd = 3300142
    group_cd = 3300142
    next_station = None
    previous_station = factory.SubFactory(PreviousStationFactory)


class TrainFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Train

    route = factory.SubFactory(RouteFactory)
    kind = "LIMITED"


class TransFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Trans

    stop = factory.SubFactory(StationFactory)
    train = factory.SubFactory(TrainFactory)
    next_stop = factory.SubFactory(PreviousStationFactory)
    leave_time = datetime(2018, 4, 22, 11, 00, 00)
    arrive_time = faker.Faker().date_time_between_dates(
        datetime_start=leave_time,
        datetime_end=None)
