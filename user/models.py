from django.db import models
from django.urls import reverse
from contests.models import Team 


class User(models.Model):
    gender = (('male', "男"), ('female', "女"),)
    name = models.CharField('账户', max_length=32, unique=True)
    password = models.CharField('密码',max_length=256)
    nickname = models.CharField('昵称',max_length=32, blank=False, default=name)
    email = models.EmailField('邮箱',unique=True)
    sex = models.CharField('性别',max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    is_activated = models.BooleanField(default=False)
    portrait = models.URLField('用户头像', blank=True)
    team = models.ForeignKey(Team, verbose_name='隶属队伍', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户对象"


# 级联删除User则删除ConfirmString，反之不可
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.name + ":   " + self.code
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码对象"