# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from applications.exercises.models import Exercise
from applications.core.presenters import BaseListPresenter

__all__ = (
    'ListExercisesView',
    'CreateExerciseView',
    'ShowExerciseView',
)


class ListExercisesView(ListView):

    model = Exercise
    template_name = 'exercises/list.html'
    context_object_name = 'exercises'

    def get_context_data(self, **kwargs):
        context = super(ListExercisesView, self).get_context_data(**kwargs)
        context.update({
            'exercises': BaseListPresenter(
                context.get('exercises'),
                title="Available Exercises",
            )
        })
        return context


class CreateExerciseView(CreateView):

    model = Exercise
    template_name = 'exercises/create.html'
    fields = ('name', 'video', 'notes')

class ShowExerciseView(DetailView):

    model = Exercise
    template_name = 'exercises/detail.html'
    context_object_name = 'exercise'
    pk_url_kwarg = 'exercise_id'

