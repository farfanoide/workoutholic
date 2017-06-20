# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.views.generic import (
    CreateView,
    ListView,
)

from applications.workouts.models import Workout
from applications.workouts.forms import WorkoutForm

__all__ = (
    'CreateWorkoutView',
    'ListWorkoutsView',
)


class ListWorkoutsView(ListView):

    model = Workout
    template_name = 'workouts/list.html'
    context_object_name = 'workouts'

class CreateWorkoutView(CreateView):

    model = Workout
    form_class = WorkoutForm
    template_name = 'workouts/create.html'
    context_object_name = 'workout'
