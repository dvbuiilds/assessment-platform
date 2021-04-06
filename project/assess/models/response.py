from django.db import models
from .candidate import candidate
from .question import question
from django.core.validators import MinValueValidator, MaxValueValidator


class responses(models.Model):
    candidate_id = models.ForeignKey(candidate, on_delete=models.PROTECT)
    q_id = models.ForeignKey(question, on_delete=models.PROTECT)
    chosen_response = models.CharField(max_length=100)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    time_taken = models.TimeField()
