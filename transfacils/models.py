from django.db import models


class Route(models.Model):
    class Meta:
        verbose_name = '路線'
        verbose_name_plural = '路線'

    TRAIN = "TRAIN"
    BUS = "BUS"
    KIND = ((BUS, 'バス'), (TRAIN, '電車'))

    name = models.CharField(max_length=30, verbose_name="路線名")
    # TODO choice
    kind = models.CharField(max_length=15, choices=KIND)
    cd = models.IntegerField(verbose_name="路線番号", primary_key=True)

    def is_train(self):
        return self.kind in self.TRAIN

    def __str__(self):
        return self.name


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
                                     blank=True, null=True)
    previous_station = models.ForeignKey('self', on_delete=models.CASCADE,
                                         related_name="previous",
                                         blank=True, null=True)

    def __str__(self):
        return self.name

    def is_end_point(self):
        return self.next_station is None

    def is_start_point(self):
        return self.previous_station is None


class Train(models.Model):
    route = models.ForeignKey("Route", on_delete=models.CASCADE, default=33001)
    stop_stations = models.ManyToManyField("Station", through='Trans',
                                           through_fields=('train', 'stop'),
                                           verbose_name="停車駅")

    TRAIN_KIND = (
        ("NORMAL", '普通'), ("RAPID", "快速"), ("EXPRESS", "急行"),
        ("LIMITED", "特急"))
    kind = models.CharField(max_length=10, choices=TRAIN_KIND,
                            verbose_name="種類", default="NORMAL")

    def __str__(self):
        return self.name() + str(self.id)

    def name(self):
        return str(self.route) + self.get_kind_display()


class Trans(models.Model):
    class Meta:
        verbose_name = '運行'
        verbose_name_plural = '運行'

    stop = models.ForeignKey("Station", on_delete=models.CASCADE,
                             related_name="stop")
    train = models.ForeignKey("Train", on_delete=models.CASCADE)
    leave_time = models.TimeField(verbose_name="出発時間")
    arrive_time = models.TimeField(verbose_name="到着時間")
    next_stop = models.ForeignKey("Station", on_delete=models.CASCADE,
                                  related_name="next_stop", blank=True)

    def __str__(self):
        return self.train.name() + str(self.stop) + str(
            self.leave_time) + "~" + str(self.next_stop) + str(
            self.arrive_time)

    def next_trans(self):
        if self.next_stop.is_end_point():
            return None
        else:
            result = self
            return result
