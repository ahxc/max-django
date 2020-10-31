from django.db import models
from django.utils.timezone import now


from user.models import User


# auto_now_add，字段创建时添加一个时间，不可修改
# auto_now，字段修改时添加一个时间，可修改
class News(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', blank=False, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    text = models.TextField('正文')
    views = models.PositiveIntegerField('浏览量', default=0)
    # released_time = models.DateTimeField('发布时间', auto_now_add=now)
    modified_time = models.DateTimeField('修改时间', auto_now=now)
    cover_url = models.URLField('封面链接', blank=True)
    def __str__(self):
        return str(self.pk)+': '+self.title
    class Meta:
        ordering = ["-modified_time"]
        verbose_name = '新闻'
        verbose_name_plural = '新闻对象'