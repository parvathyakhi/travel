from django.db import models

# Create your models here.
class place(models.Model):
    # objects = None
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    nam = models.CharField(max_length=250)
    ig = models.ImageField(upload_to='pic')
    des = models.TextField()

    def __str__(self):
        return self.nam