from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    userPic = models.ImageField(upload_to='profilePics', blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
