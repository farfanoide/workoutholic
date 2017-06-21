# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from applications.workouts.models import Workout, Segment, WorkoutType
from applications.workouts.forms import (
    SegmentExerciseFormSet,
    SegmentForm,
    WorkoutForm,
)
from applications.core.presenters import BaseListPresenter

__all__ = (
    'AddSegmentView',
    'CreateWorkoutView',
    'EditSegmentView',
    'ListWorkoutsView',
    'ShowSegmentView',
    'ShowWorkoutView',
)


class ListWorkoutsView(ListView):

    model = Workout
    template_name = 'workouts/list.html'
    context_object_name = 'workouts'

    def get_context_data(self, **kwargs):
        context = super(ListWorkoutsView, self).get_context_data(**kwargs)
        context.update({
            'workouts': BaseListPresenter(
                context.get('workouts'),
                title="Available Workouts",
            )
        })
        return context

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

class EditSegmentView(DetailView):

    model = Segment
    template_name = 'segments/edit.html'
    context_object_name = 'segment'
    pk_url_kwarg = 'segment_id'

    def get_formset(self):
        formset_kwargs = {
            'queryset': self.get_segment().segmentexercise_set.all()
        }

        if self.request.method == 'POST':
            formset_kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES
            })

        formset = SegmentExerciseFormSet(**formset_kwargs)

        for form in formset:
            form.instance.segment = self.get_segment()
        return formset

    def get_segment(self):
        if not hasattr(self, '_segment'):
            self._segment = Segment.objects.get(pk=self.kwargs.get('segment_id'))
        return self._segment

    def get_context_data(self, **kwargs):
        self.object = self.get_segment()
        context = super(EditSegmentView, self).get_context_data(**kwargs)
        context.update({
            'formset': self.get_formset()
        })
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('workouts:show', kwargs={
                'workout_id': self.kwargs.get('workout_id')
            }))
        else:
            return self.render_to_response(
                self.get_context_data(formset=formset)
            )
