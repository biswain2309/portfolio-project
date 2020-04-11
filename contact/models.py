from django.db import models

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')
    dtl = models.CharField(max_length=100,blank=True, null=True)
    urls = models.TextField(blank=True, null=True)