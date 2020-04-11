from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]

    def urls(self):
        return self.url
