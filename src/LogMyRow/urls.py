from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from workouts.views import (
    WorkoutCreateView,
    WorkoutListView,
    WorkoutDetailView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WorkoutCreateView.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^workouts/$', WorkoutListView.as_view()),
    url(r'^workouts/(?P<workout_id>\w+)/$', WorkoutDetailView.as_view()),
]
