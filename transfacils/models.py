from django.contrib.postgres.fields import ArrayField
from django.db import models


class Route(models.Model):
    class Meta:
        verbose_name = '路線'
        verbose_name_plural = '路線'

    name = models.CharField(max_length=30, verbose_name="路線名")
    # TODO choice
    kind = models.CharField(max_length=15)
    cd = models.IntegerField(verbose_name="路線番号", primary_key=True, )

    def stop_stations(self):
        stations = self.transes.all()
        return stations

    def __str__(self):
        return self.name


class Trans(models.Model):
    class Meta:
        verbose_name = '運行'
        verbose_name_plural = '運行'

    route = models.ForeignKey("Route", on_delete=models.CASCADE,
                              related_name="transes")
    stations = ArrayField(models.IntegerField(), blank=True)


class Station(models.Model):
    class Meta:
        verbose_name = '駅'
        verbose_name_plural = '駅'

    name = models.CharField(max_length=30)
    route = models.ForeignKey("Route", on_delete=models.CASCADE,
                              related_name="stations")
    cd = models.IntegerField(verbose_name="駅番号", primary_key=True, unique=True)
    group_cd = models.IntegerField(verbose_name="グループ番号")
    # TODO on_delete を変化させる
    next_station = models.ForeignKey('self', on_delete=models.CASCADE,
                                     related_name="next",
                                     null=True)
    previous_station = models.ForeignKey('self', on_delete=models.CASCADE,
                                         related_name="previous",
                                         null=True)

    def __str__(self):
        return self.name

# @receiver(pre_save, sender=Station)
# def set_next_station(sender, **kwargs):
#     sender.next_station_id = sender.id if sender.next_station is None else sender.next_station_id


# @receiver(pre_save, sender=Station)
# def set_previous_station(sender, **kwargs):
#     sender.previous_station_id = sender.id if sender.previous_station is None else sender.previous_station_id
