from django.db import models

# Create your models here.
class RowingWorkout(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=120)
    meters = models.CharField(max_length=120)
    notes = models.CharField(max_length=420)
    def __str__(self):
        return str(self.date)
