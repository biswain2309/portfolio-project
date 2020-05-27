from django.db import models


class Achievements(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    completion_date = models.DateField()