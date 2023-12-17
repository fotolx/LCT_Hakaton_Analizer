from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)
    author = models.BooleanField(default=True)
    subsribed_to_newsletter = models.BooleanField(default=False)
    mail_confirmed = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'
    
    def update_rating(self):
        pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='account.png', upload_to='images/profile/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
