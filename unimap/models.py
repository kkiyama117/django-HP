from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from model_utils.managers import InheritanceManager


class Place(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False,
                            unique=True)
    objects = InheritanceManager()
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class University(Place):
    """大学を表すクラス"""
    slug = models.SlugField(max_length=256)


class Campus(Place):
    """キャンパスを表すクラス"""
    name = models.CharField(max_length=256)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    group = models.CharField(max_length=128, default=name)


class Building(Place):
    """建物を表すクラス"""
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)


class Room(Place):
    """部屋を表す"""
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    # Validator はmodelformを使うときだけ
    floor = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
