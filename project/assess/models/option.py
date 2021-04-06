from django.db import models
from .course import course
from django.core.validators import MaxValueValidator, MinValueValidator
from .question import question

class options(models.Model):
    optA = models.CharField(max_length=100)
    optB = models.CharField(max_length=100)
    optC = models.CharField(max_length=100)
    optD = models.CharField(max_length=100)
    correct_opt = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    ques_id = models.ForeignKey(question, on_delete=models.PROTECT)
    course_id = models.ForeignKey(course, on_delete=models.PROTECT)