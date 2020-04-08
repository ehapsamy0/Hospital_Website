from django.db import models

# Create your models here.


class Department(models.Model):
    name    = models.CharField(max_length=250)
    image   = models.ImageField(upload_to='department_img/')
    description = models.TextField()


    def __str__(self):
        return self.name