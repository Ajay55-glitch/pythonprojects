from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField(default=0)


    def __str__(self):
        return self.name
class Names(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField(default=0)


    def __str__(self):
        return self.name



