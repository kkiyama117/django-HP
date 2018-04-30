from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class University(Place):
    slug = models.SlugField(max_length=256)
