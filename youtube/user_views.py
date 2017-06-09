from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests

# Register
def register(request):
	context = {
	}
	return render(request, "register.html", context)

def create_user(request):
	user = User()

	username = request.POST["username"]
	email = request.POST["email"]
	password = request.POST["password"]
	password_confirm = request.POST["password_confirm"]

	user = User.objects.create_user(username, email, password)

	context = {
		"users": User.objects.all()
	}

	user.save()
	return render(request, "create_user.html", context)

# Sign in
def sign_in(request):
	context = {}

	if "username" in request.POST and "password" in request.POST:
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)

		try:
			login(request, user)
			if user is not None:
				return HttpResponsePermanentRedirect("/youtube/index")
		except:
			return render(request, "sign_in.html", context)

	return render(request, "sign_in.html", context)

# Sign out
def sign_out(request):
	logout(request)
	context = {
	}
	return render(request, "sign_out.html", context)

# Login success
def login_success(request):
	logout(request)
	context = {
	}
	return render(request, "login_success.html", context)