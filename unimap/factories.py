import factory

from unimap import models


class UniversityFactory(factory.DjangoModelFactory):
    name = 'Kyoto_Univ'
    slug = "KU"
    longitude = 0.0
    latitude = 0.0

    class Meta:
        model = models.University


class CampusFactory(factory.DjangoModelFactory):
    name = "Yoshida-South"
    group = "Yoshida"
    longitude = 0.0
    latitude = 0.0
    university = factory.SubFactory(UniversityFactory)

    class Meta:
        model = models.Campus


class BuildingFactory(factory.DjangoModelFactory):
    name = "Yoshida-South Campus Academic Center Bldg North Wing"
    longitude = 0.0
    latitude = 0.0
    campus = factory.SubFactory(CampusFactory)

    class Meta:
        model = models.Building


class RoomFactory(factory.DjangoModelFactory):
    name = "Kyokita22"
    longitude = 0.0
    latitude = 0.0
    floor = 2
    building = factory.SubFactory(BuildingFactory)

    class Meta:
        model = models.Room
