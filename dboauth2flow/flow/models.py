from django.db import models
from django.contrib.auth.models import User

class DropboxToken(models.Model):
    user = models.OneToOneField(User,related_name="dbx")
    access_token = models.CharField(max_length=256)