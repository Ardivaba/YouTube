from django.db import models

from django.contrib.auth.models import User

# Blinks
class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=2000)
	video_url = models.CharField(max_length=2000)

	def __str__(self):
		return self.title + " - " + self.description + " - " + self.video_url
