from django.conf.urls import url, include
from django.contrib import admin
from . import views
from . import user_views

urlpatterns = [
    url(r'^index', views.index),

    # User system
	url(r"^sign_in", user_views.sign_in, name = "sign_in"),
	url(r"^sign_out", user_views.sign_out, name = "sign_out"),
	url(r"^register", user_views.register, name = "register"),
	url(r"^create_user", user_views.create_user, name = "create_user"),
]