from django.db import models


class Route(models.Model):
    class Meta:
        verbose_name = '路線'
        verbose_name_plural = '路線'

    name = models.CharField(max_length=30, verbose_name="路線名")
    # TODO choice
    kind = models.CharField(max_length=15)

    def stop_stations(self):
        stations = self.transes.all()
        return stations

    def __str__(self):
        return self.name


class Trans(models.Model):
    route = models.ForeignKey("Route", on_delete=models.CASCADE,
                              related_name="transes")
    # related_name を違う文脈で使う.
    # ただ逆参照を混ぜないためだけ
    leave_from = models.ForeignKey("Station", on_delete=models.CASCADE,
                                   related_name="leave")
    arrive_at = models.ForeignKey("Station", on_delete=models.CASCADE,
                                  related_name="arrive")


class Station(models.Model):
    class Meta:
        verbose_name = '駅'
        verbose_name_plural = '駅'

    name = models.CharField(max_length=30)
    route = models.ForeignKey("Route", on_delete=models.CASCADE,
                              related_name="stations")
    # TODO on_delete を変化させる
    next_station = models.ForeignKey('self', on_delete=models.CASCADE,
                                     related_name="next",
                                     blank=True, null=True)
    previous_station = models.ForeignKey('self', on_delete=models.CASCADE,
                                         related_name="previous",
                                         blank=True, null=True)
    time_to_next_station = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Override default save method

        Args:
            *args (array):  args
            **kwargs (array):   args

        """
        if self.next_station is None:
            self.next_station_id=self.id
        if self.previous_station is None:
            self.previous_station_id=self.id
        super(Station, self).save(args, kwargs)
