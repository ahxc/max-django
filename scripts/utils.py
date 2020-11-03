import hashlib
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from pytz import timezone
from rest_framework.serializers import Field
from rest_framework.pagination import PageNumberPagination


from user import models


# sha256算法
# 加点盐（噪）
# update方法只接收bytes类型
def hash_code(s):#, salt='max'
    # s += salt
    h = hashlib.sha256(s.encode())
    return h.hexdigest()


# MD5算法
def get_md5(s):
    m = hashlib.md5(s.encode('utf-8'))
    return m.hexdigest()


def make_confirm_string(user):
    code = hash_code(user.name)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code


def send_email(email, code):
    subject = '注册验证邮件'
    html_content = '''邮箱验证链接："http://{}/confirm/?code={}"，此链接有效期为{}天！'''\
    .format('192.168.3.82:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, html_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# 时间转时间戳类
class TimestampField(Field):
    def to_representation(self, value):
        return int(value.timestamp())


# 分页定制类
class ListPagination(PageNumberPagination):
    page_size = 10# 表示每页的默认显示数量
    # page_size_query_param = 'page_size'# 表示url中每页请求数量，可以不加到url中
    page_query_param = 'page'# 表示url中的页码参数
    max_page_size = 100# 表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃


class allPagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    max_page_size = 100