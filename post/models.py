from django.db import models
from django.utils.timezone import now


from user.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='分类', max_length=30, unique=True)
    category_icon = models.URLField(verbose_name='分类图标', blank=True)
    parents_category = models.ForeignKey('self', verbose_name='父类', blank=True, null=True, on_delete=models.CASCADE)
    is_parents = models.BooleanField(verbose_name='是否父级分类', default=False, blank=False)
    describe = models.CharField(verbose_name='描述', max_length=40, blank=True, null=True)
    def __str__(self):
        if self.parents_category == None and self.is_parents:
            return str(self.pk)+': '+self.name
        else:
            return str(self.pk)+': '+self.name+'({})'.format(self.parents_category.name)
    class Meta:
        ordering = ['pk']
        verbose_name = '分类'
        verbose_name_plural = '分类对象'


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name='分类', blank=False, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    text = models.TextField('正文')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞量', default=0)
    modified_time = models.DateTimeField('发布时间', auto_now=now)
    def __str__(self):
        return str(self.pk)+': '+self.title
    class Meta:
        ordering = ['-modified_time']
        verbose_name = '帖子'
        verbose_name_plural = '帖子对象'