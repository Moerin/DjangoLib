from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    file_path = models.FileField(upload_to='uploads/')
