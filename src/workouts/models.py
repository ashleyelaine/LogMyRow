from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class RowingWorkout(models.Model):
    owner = models.ForeignKey(User)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.IntegerField()
    meters = models.IntegerField()
    notes = models.CharField(max_length=420, null=True, blank=True)
    def __str__(self):
        return str(self.date)
