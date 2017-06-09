from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import Video
import requests

# Add video
def add_video(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, "add_video.html", {
            "uploaded_file_url": uploaded_file_url
        })

	return render(request, "add_video.html", {})

def videos(request):
	videos = Video.objects.all()
	no_videos = False
	if len(videos) < 1:
		no_videos = True
	return render(request, "videos.html", {
		"videos": Video.objects.filter(user = request.user),
		"no_videos": no_videos
	})

def add_video(request):

	if request.method == "POST" and request.FILES["video"]:
		video_file = request.FILES["video"]
		fs = FileSystemStorage()
		file_name = fs.save(video_file.name, video_file)
		uploaded_file_url = fs.url(file_name)

		video = Video()

		video.user = request.user
		video.title = request.POST["title"]
		video.description = request.POST["description"]
		video.video_url = uploaded_file_url

		video.save()

		return render(request, "add_video.html", {
			"uploaded_file_url": uploaded_file_url
		})

	return render(request, "add_video.html", {})