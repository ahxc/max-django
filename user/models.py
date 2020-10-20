from django.db import models
from django.urls import reverse

class User(models.Model):
  gender = (('Y', "男"), ('X', "女"),)
  name = models.CharField('账户', max_length=128, unique=True)
  password = models.CharField('密码', max_length=256)
  email = models.EmailField('电子邮箱', unique=True)
  sex = models.CharField('性别', max_length=32, choices=gender, default="男")
  c_time = models.DateTimeField('创建时间', auto_now_add=True)
  def __str__(self):
    return self.name
  class Meta:
    ordering = ["-c_time"]
    verbose_name = "用户"
    verbose_name_plural = "用户对象"