import hashlib
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from user import models


# sha256算法
# 加点盐（噪）
# update方法只接收bytes类型
def hash_code(s, salt='mysite'):
	s += salt
	h = hashlib.sha256(s.encode())
	return h.hexdigest()


# MD5算法
def get_md5(s):
	m = hashlib.md5(s.encode('utf-8'))
	return m.hexdigest()


def make_confirm_string(user):
	now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	code = hash_code(user.name, now_time)
	models.ConfirmString.objects.create(code=code, user=user,)
	return code


def send_email(email, code):
	subject = '注册验证邮件'
	html_content = '''邮箱验证链接："http://{}/confirm/?code={}"，此链接有效期为{}天！'''\
	.format('192.168.3.82:8000', code, settings.CONFIRM_DAYS)
	msg = EmailMultiAlternatives(subject, html_content, settings.EMAIL_HOST_USER, [email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()