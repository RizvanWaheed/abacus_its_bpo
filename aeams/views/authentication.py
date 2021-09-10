#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import auth # authenticate, login, logout
from recruitment.views import *


def login(request):
	# print(request)
	# if request.Users.is_authenticated:
	# 	return render(request, 'recruitment/index.html')
	if request.method=='POST':
		# print(request.POST)
		user = auth.authenticate(request, username=request.POST['login'] , password=request.POST['password'])
		if user is not None:
			# print(user)
			auth.login(request, user)
			# print("Logged In")
			# print(user)
			request.session['is_logged']=True
			return redirect('/aeams/dashboard')
		else:
			return render(request, 'login.html', {'error': 'Username or Password is incorrect!!!'})
	else:
		return render(request, 'login.html')




def logout(request):
	# if request.method=='GET':
    auth.logout(request)
    return redirect('login')
	# else:
	# 	return render(request,'logout.html')

