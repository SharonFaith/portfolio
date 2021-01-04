from django.db import models
import datetime as dt
import cloudinary 
from cloudinary.models import CloudinaryField

class Project(models.Model):
    name = models.CharField(max_length=30)
    landing_page = CloudinaryField(blank=True, null=True)
    description = models.TextField()
    live_site = models.URLField(blank=True)
    repo_link = models.URLField()