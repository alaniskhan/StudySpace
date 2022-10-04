
from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(blank=True)
    video_url = models.URLField(blank=True)
    img = models.ImageField(default='/TOEFL-Study-Material_Ec4iBJ5.jpg', blank=True)