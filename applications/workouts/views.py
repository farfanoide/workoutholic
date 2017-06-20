# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from applications.workouts.models import Workout, Segment, WorkoutType
from applications.workouts.forms import WorkoutForm, SegmentForm

__all__ = (
    'AddSegmentView',
    'CreateWorkoutView',
    'ListWorkoutsView',
    'ShowSegmentView',
    'ShowWorkoutView',
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

class ShowWorkoutView(DetailView):

    model = Workout
    template_name = 'workouts/detail.html'
    context_object_name = 'workout'
    pk_url_kwarg = 'workout_id'

class AddSegmentView(CreateView):

    model = Segment
    form_class = SegmentForm
    template_name = 'workouts/add_segment.html'
    context_object_name = 'segment'

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(AddSegmentView, self).get_form_kwargs(**kwargs)
        initial = form_kwargs.get('initial', {})
        initial.update({'workout': self.kwargs.get('workout_id')})
        form_kwargs.update({'initial': initial})
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(AddSegmentView, self).get_context_data(**kwargs)
        context.update({'workout': self.get_workout()})
        return context

    def get_workout(self):
        if not hasattr(self, '_workout'):
            self._workout = Workout.objects.get(pk=self.kwargs.get('workout_id'))
        return self._workout



class ShowSegmentView(DetailView):

    model = Segment
    template_name = 'segments/detail.html'
    context_object_name = 'segment'
    pk_url_kwarg = 'segment_id'
