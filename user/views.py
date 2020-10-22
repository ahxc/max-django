import datetime
from django.shortcuts import render, redirect
from django.conf import settings

from scripts.utils import hash_code, send_email, make_confirm_string
from . import models, forms


def index(request):
	if not request.session.get('is_login', None):
		return redirect('/login/')
	return render(request, 'login/index.html')


# locals返回本地的所有变量字典，不用再编写数据字典，重新递交也不会丢失除密码以外的信息，但会递交全部变量引起冗余
# session会话你完全可以往里面写任何数据，不仅仅限于用户相关！
# get方法关联表单建立样式
def login(request):
	if request.session.get('is_login', None):# 不允许重复登录
		return redirect('/index/')
	if request.method == 'POST':
		login_form = forms.UserForm(request.POST)
		message = '请检查填写的内容！'
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			try:
				user = models.User.objects.get(name=username)
			except :
				message = '用户不存在！'
				return render(request, 'login/login.html', locals())
			if not user.is_activated:
				message = '该用户还未激活，请前往注册邮箱确认激活！'
				return render(request, 'login/login.html', locals())
			if user.password == hash_code(password):
				request.session['is_login'] = True
				request.session['user_id'] = user.id
				request.session['user_name'] = user.name
				return redirect('/index/')
			else:
				message = '密码不正确！'
				return render(request, 'login/login.html', locals())
		else:
			return render(request, 'login/login.html', locals())
	login_form = forms.UserForm()
	return render(request, 'login/login.html', locals())


# is_valid一步完成数据合法性验证工作
def register(request):
	if request.session.get('is_login', None):
		return redirect('/index/')
	if request.method == 'POST':
		register_form = forms.RegisterForm(request.POST)
		message = "请检查填写的内容！"
		if register_form.is_valid():
			username = register_form.cleaned_data.get('username')
			password1 = register_form.cleaned_data.get('password1')
			password2 = register_form.cleaned_data.get('password2')
			email = register_form.cleaned_data.get('email')
			sex = register_form.cleaned_data.get('sex')
			if password1 != password2:
				message = '两次密码不一致！'
				return render(request, 'login/register.html', locals())
			else:
				same_name_user = models.User.objects.filter(name=username)
				if same_name_user:
					message = '用户名已经存在'
					return render(request, 'login/register.html', locals())
				same_email_user = models.User.objects.filter(email=email)
				if same_email_user:
					message = '该邮箱已被注册！'
					return render(request, 'login/register.html', locals())
				new_user = models.User()
				new_user.name = username
				new_user.password = hash_code(password1)
				new_user.email = email
				new_user.sex = sex
				new_user.save()
				code = make_confirm_string(new_user)
				send_email(email, code)
				return redirect('/login/')
		else:
			return render(request, 'login/register.html', locals())
	register_form = forms.RegisterForm()
	return render(request, 'login/register.html', locals())


# flush一次性将session中的所有内容全部清空，是操作会话比较安全的一种做法，缺点会话会全部清空
# 或者使用下面的方法
# del request.session['is_login']
# del request.session['user_id']
# del request.session['user_name']
def logout(request):
	if not request.session.get('is_login', None):
		return redirect("/login/")
	request.session.flush()
	return redirect("/login/")


# 获得请求query参数中的code
# 通过OneToOneFile获取user.save并存储
def user_confirm(request):
	code = request.GET.get('code', None)
	message = ''
	try:
		confirm = models.ConfirmString.objects.get(code=code)
	except:
		message = '无效的确认请求!'
		return render(request, 'login/confirm.html', locals())
	c_time = confirm.c_time
	now = datetime.datetime.now()
	if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
		confirm.user.delete()
		message = '验证邮件已过期！请重新注册!'
		return render(request, 'login/confirm.html', locals())
	else:
		confirm.user.is_activated = True
		confirm.user.save()
		confirm.delete()
		message = '注册验证成功！'
		return render(request, 'login/confirm.html', locals())