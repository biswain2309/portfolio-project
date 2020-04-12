from django.db import models


class Achievements(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
