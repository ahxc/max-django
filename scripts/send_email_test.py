import os, sys
from django.core.mail import EmailMultiAlternatives

back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'max.settings'

if __name__ == '__main__':
	subject, from_email, to = '这是一封邮件发送配置测试邮件', 'ahxc1020@qq.com', 'ahxc1020@gmail.com'
	text_content = """请不要答复该邮件，链接点击测试http://www.baidu.com"""
	# html_content = '<p>链接点击测试<a href="http://www.baidu.com" target=blank>www.baidu.com</a></p>'
	msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
	# msg.attach_alternative(html_content, "text/html")
	msg.send()