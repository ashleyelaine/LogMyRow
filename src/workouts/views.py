from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RowingWorkoutCreateForm
from .models import RowingWorkout

# CREATE WORKOUT FORM VIEW [HOME]
class WorkoutCreateView(LoginRequiredMixin, CreateView):
    form_class = RowingWorkoutCreateForm
    template_name = 'workouts/form.html'
    success_url = "/workouts/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(WorkoutCreateView, self).form_valid(form)

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
