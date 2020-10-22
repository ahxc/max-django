from django.db import models
from django.utils.timezone import now


class Contests(models.Model):
    start_time = models.DateTimeField('开始时间', blank=False, null=False, default=now)
    end_time = models.DateTimeField('结束时间', blank=False, null=False, default=now)
    game_type = models.CharField('举办类型', max_length=200)
    def __str__(self):
        return self.game_type
    class Meta:
        ordering = ["game_type"]
        verbose_name = '赛事'
        verbose_name_plural = '赛事对象'


class Team(models.Model):
    name = models.CharField('队名', blank=False, max_length=64, unique=True)
    contests = models.ManyToManyField('Contests', verbose_name="赛事", blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = '队伍'
        verbose_name_plural = '队伍对象'