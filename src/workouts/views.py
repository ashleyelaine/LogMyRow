from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RowingWorkoutCreateForm
from .models import RowingWorkout

# CREATE WORKOUT FORM VIEW [HOME]
class WorkoutCreateView(CreateView):
    form_class = RowingWorkoutCreateForm
    template_name = 'workouts/form.html'
    success_url = "/workouts/"

# WORKOUTS LIST VIEW
class WorkoutListView(ListView):
    def get_queryset(self):
        queryset = RowingWorkout.objects.all()
        return queryset

# WORKOUTS SINGLE VIEW
class WorkoutDetailView(DetailView):
    queryset = RowingWorkout.objects.all()

    def get_object(self, *args, **kwargs):
        workout_id = self.kwargs.get('workout_id')
        obj = get_object_or_404(RowingWorkout, id=workout_id)
        return obj
