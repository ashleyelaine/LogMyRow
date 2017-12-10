from django.forms import ModelForm, Textarea, SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from .models import RowingWorkout

class RowingWorkoutCreateForm(ModelForm):
    class Meta:
        model = RowingWorkout
        fields = ('date','time','meters','notes')
        labels = {
            'time': _('Total Time (min)'),
            'meters': _('Total Meters'),
        }
        widgets = {
            'date': SelectDateWidget(),
            'notes': Textarea(attrs={'cols': 40, 'rows': 3}),
        }
