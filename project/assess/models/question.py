from django.db import models
from .course import course

class question(models.Model):
    ques_body = models.CharField(max_length=200)
    ques_id = models.ForeignKey(course, on_delete=models.PROTECT)
