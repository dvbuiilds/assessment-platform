from django.db import models
from .candidate import candidate
from .course import course

class assessments(models.Model):
    candidate_id = models.ForeignKey(candidate, on_delete=models.PROTECT)
    candidate_fname = models.CharField(max_length=20)
    candidate_lname = models.CharField(max_length=20)
    assess_course = models.ForeignKey(course, on_delete=models.PROTECT)
    date_of_assess = models.DateTimeField()
    score = models.IntegerField()
    total_time = models.TimeField()