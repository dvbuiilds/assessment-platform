from django.db import models

class course(models.Model):
    name = models.CharField(max_length=20)