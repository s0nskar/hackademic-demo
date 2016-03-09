from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from hackademic.forms import UserForm

def register(request):
	context = {}

	if request.method == "POST":

		#getting data form POST request
		user_form = UserForm(data=request.POST)
		type_ = request.POST['type']

		#define types i.e. defined groups
		dtypes = ['Student', 'Teacher', 'Admin']

		if user_form.is_valid() and type_ in dtypes:
			user = user_form.save()
			user.set_password(user.password)
			
			#Trying to get groups corresponding to given type
			try:
				group = Group.objects.get(name=type_)
			except Group.DoesNotExist as e:
				print "[*] Please create group named {0}".format(type_)
				return HttpResponse(e)

			user.groups.add(group)
			user.save()
			return redirect('user')

		else:
			context['user_form'] = user_form
			context['msg'] = user_form.errors

	else:
		user_form = UserForm()
		context['user_form'] = user_form

	#Render the register.html template
	return render(request, 'register.html', context)

def login(request):
	context = {}

	if request.method == "POST":
		username = request.POST['username']
		pwd = request.POST['pwd']

		#Checking username and password
		user = authenticate(username=username, password=pwd)

		#if credentials are correct
		if user:
			if user.is_active:
				#logging user in
				auth_login(request, user)
				return redirect('user')
			else:
				context['msg'] = "Your account is disabeled!!"
				return render(request, 'login.html', context)
		#Credentials don't match	
		else:
			print "[*] Invalid login details: {0}, {1}".format(username, pwd)
			context['msg'] = "Invalid login details"
			return render(request, 'login.html', context)
	else:
		return render(request, 'login.html', context)

@login_required
def logout(request):
	context = {}
	auth_logout(request)
	return redirect('index')

def index(request):
	return render(request, 'index.html', {})

@login_required
def user(request):
	u = request.user
	try:
		group = u.groups.get().name
		print group
	except Group.MultipleObjectsReturned as e:
		return HttpResponse(e)
	return render(request, 'user.html', {'group':group, 'u':u})