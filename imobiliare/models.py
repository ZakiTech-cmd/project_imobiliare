from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Announce(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    floor = models.IntegerField(null=True)
    county = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        ordering = ['-last_update', '-publish_date']
#  functii care sunt declarate in interiorul clasei se numesc metode,
#  Getter de titlu
    def __str__(self):
        return self.title 