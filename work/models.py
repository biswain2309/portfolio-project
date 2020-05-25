from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=200)
    tech = models.CharField(max_length=200)
    body = models.TextField()
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body

    def urls(self):
        return self.url

    def __str__(self):
        return self.tech