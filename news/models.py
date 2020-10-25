from django.db import models
from django.utils.timezone import now


from user.models import User


class News(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', blank=False, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    text = models.TextField('正文')
    views = models.PositiveIntegerField('浏览量', default=0)
    released_time = models.DateTimeField('发布时间', blank=False, null=False, default=now)
    cover_url = models.URLField('封面链接', blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    class Meta:
        ordering = ["-released_time"]
        verbose_name = '新闻'
        verbose_name_plural = '新闻对象'