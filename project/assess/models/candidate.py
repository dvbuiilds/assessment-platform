from django.db import models

class candidate(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    ph_no = models.CharField(max_length=10)
    email = models.EmailField()
