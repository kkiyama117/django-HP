from django.db import models


class University(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.name
