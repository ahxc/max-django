from django.db import models
from django.utils.timezone import now


# 大型赛事对象
class Contests(models.Model):
    contests_name = models.CharField('赛事名称', blank=False, max_length=64, unique=True)
    start_time = models.DateTimeField('开始时间', blank=False, null=False, default=now)
    end_time = models.DateTimeField('结束时间', blank=False, null=False, default=now)
    team = models.ManyToManyField('Team', verbose_name='参赛队伍', through='Game')
    is_end = models.BooleanField('是否结束', default=False)
    def __str__(self):
        return self.contests_name
    class Meta:
        ordering = ["contests_name"]
        verbose_name = '赛事'
        verbose_name_plural = '赛事对象'


# 每场比赛对象
class Game(models.Model):
    choices = ((0, '进行中'), (1, '获胜'), (2, '失败'))
    game_status = models.SmallIntegerField(choices=choices, default=0, verbose_name='比赛状态')
    code = models.CharField('比赛编码', max_length=10, blank=False)
    start_time = models.DateTimeField('开始时间', blank=False, default=now)
    end_time = models.DateTimeField('结束时间', blank=False, default=now)
    contests = models.ForeignKey('Contests', verbose_name='赛事', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', verbose_name='参赛一方', on_delete=models.CASCADE)
    def __str__(self):
        return self.contests.contests_name+": "+self.code
    class Meta:
        ordering = ["code"]
        verbose_name = '比赛'
        verbose_name_plural = '比赛对象'


# 参赛队伍
class Team(models.Model):
    logo = models.URLField('队标', blank=True)
    name = models.CharField('队名', blank=False, max_length=64, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = '队伍'
        verbose_name_plural = '队伍对象'