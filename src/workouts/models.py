from django.db import models

# Create your models here.
class RowingWorkout(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.IntegerField()
    meters = models.IntegerField()
    notes = models.CharField(max_length=420, null=True, blank=True)
    def __str__(self):
        return str(self.date)
