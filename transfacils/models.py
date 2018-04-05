from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=15)

    def stop_stations(self):
        stations = self.transes.all()
        return stations


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
    name = models.CharField(max_length=30)
    route = models.ForeignKey("Route", on_delete=models.CASCADE,
                              related_name="stations")
    # TODO on_delete を変化させる
    next_station = models.ForeignKey('self', on_delete=models.CASCADE)
    time_to_next_station = models.DateTimeField()

    def get_next_station(cls):
        yield cls.next_station
