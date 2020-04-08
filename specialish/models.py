from django.db import models

# Create your models here.


class Specialish(models.Model):
    name = models.CharField(max_length=250)
    title_jop = models.CharField(max_length=250)
    image = models.ImageField(upload_to='doctor_image/')
    bio = models.TextField()
    facbook_url = models.URLField(default='facebook.com',null=True,blank=True)
    pinterest_url = models.URLField(default='pinterest.com',null=True,blank=True)
    linkedin_url = models.URLField(default='linkedin.com',null=True,blank=True)
    twitter_url = models.URLField(default='twitter.com',null=True,blank=True)


    def __str__(self):
        return self.name





