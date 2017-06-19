# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.views.generic import (
    CreateView,
    CreateView,
    DetailView,
    ListView,
)

from applications.exercises.models import Exercise

__all__ = (
    'ListExercisesView',
    'CreateExerciseView',
    'ShowExerciseView',
)


class ListExercisesView(ListView):

    model = Exercise
    template_name = 'exercises/list.html'
    context_object_name = 'exercises'

class CreateExerciseView(CreateView):

    model = Exercise
    template_name = 'exercises/create.html'
    fields = ('name', 'video', 'notes')

class ShowExerciseView(DetailView):

    model = Exercise
    template_name = 'exercises/detail.html'
    context_object_name = 'exercise'
    pk_url_kwarg = 'exercise_id'

