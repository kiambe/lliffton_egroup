from django.db import models

# Create your models here.
length = 3000


class Sessions(models.Model):
    id = models.AutoField(primary_key=True)
    phoneNumber = models.CharField(
        max_length=length, default="", null=True, blank=True)
    sessionNumber = models.CharField(
        max_length=length, default="", null=True, blank=True)
    text = models.CharField(
        max_length=length, default="", null=True, blank=True)
    response = models.CharField(
        max_length=length, default="", null=True, blank=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sessionNumber}"