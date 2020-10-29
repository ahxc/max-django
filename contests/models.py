from django.db import models
from django.utils.timezone import now


class Commentary(models.Model):
    time = models.DateTimeField('赛点时间', blank=False, default=now)
    story = models.CharField('赛点情况', max_length=200, blank=False, default=None)
    game = models.ForeignKey('Game', verbose_name='所属比赛', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.story[:10]
    class Meta:
        ordering = ["time"]
        verbose_name = '赛点'
        verbose_name_plural = '赛点对象'


# 大型赛事对象
class Contests(models.Model):
    contests_name = models.CharField('赛事名称', blank=False, max_length=32, unique=True)
    start_time = models.DateTimeField('开始时间', blank=False, default=now)
    end_time = models.DateTimeField('结束时间', blank=False, default=now)
    is_end = models.BooleanField('是否结束', default=False)
    def __str__(self):
        return self.contests_name
    class Meta:
        ordering = ["-start_time"]
        verbose_name = '赛事'
        verbose_name_plural = '赛事对象'


# 每场比赛对象
class Game(models.Model):
    choices = ((0,'红队胜'),(1,'蓝队胜'),(2, '平局'))
    game_status = models.SmallIntegerField(choices=choices, default=0, verbose_name='比赛状态')
    is_end = models.BooleanField('是否结束', default=False)
    start_time = models.DateTimeField('开始时间', blank=False, default=now)
    end_time = models.DateTimeField('结束时间', blank=False, default=now)
    contests = models.ForeignKey('Contests', verbose_name='赛事', on_delete=models.CASCADE, blank=False)
    r_team = models.ForeignKey('Team', verbose_name='红队', on_delete=models.CASCADE, related_name='r_team')
    b_team = models.ForeignKey('Team', verbose_name='蓝队', on_delete=models.CASCADE, related_name='b_team')
    def __str__(self):
        return self.contests.contests_name+": "+str(self.pk)
    class Meta:
        ordering = ["-start_time"]
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