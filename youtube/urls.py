from django.conf.urls import url, include
from django.contrib import admin

from . import views
from . import user_views
from . import video_views

urlpatterns = [
	url(r"^$", views.index, name = "index"),
    url(r'^index', views.index),

    # User system
	url(r"^sign_in", user_views.sign_in, name = "sign_in"),
	url(r"^sign_out", user_views.sign_out, name = "sign_out"),
	url(r"^register", user_views.register, name = "register"),
	url(r"^create_user", user_views.create_user, name = "create_user"),
	url(r"^login_success", user_views.login_success, name = "login_success"),

	# Videos
	url(r"^add_video", video_views.add_video, name = "add_video")
]