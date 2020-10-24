from django.db import models
from django.urls import reverse
from contests.models import Team 


# django默认会以模型的小写加上_set作为反向关联名：team.user_set
# 自定义可在related_name中设置，关闭反向关联使用'+'或者名称后加'+'
# auto_now_add后台将不可编辑
class User(models.Model):
    gender = ((1, "男"), (0, "女"),)
    name = models.CharField('账户', max_length=32, unique=True)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('昵称', max_length=16, blank=False, default=name)
    email = models.EmailField('邮箱', unique=True)
    sex = models.SmallIntegerField('性别', max_length=32, choices=gender, default="男")
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
        return self.user.name + "：" + self.code
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码对象"