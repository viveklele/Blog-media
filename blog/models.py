from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	blog_image = models.ImageField(default='default_blog.jpg' ,upload_to='blog_pics')
	audio = models.FileField(default="No audio posted", upload_to='audio_files')
	video = models.FileField(default="No video posted", upload_to='video_files')

	
	def __str__(self):
		return self.title
		
	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
		
		