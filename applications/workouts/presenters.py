# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.core.urlresolvers import reverse

from applications.core.presenters import BasePresenter, BaseListPresenter

from applications.exercises.presenters import ExercisePresenter

__all__ = (
    'SegmentPresenter',
    'WorkoutPresenter',
)


class WorkoutPresenter(BasePresenter):

    templates_base_dir = 'workouts/presenters/'
    template_presented_name = 'workout'

    def get_context(self):
        context = super(WorkoutPresenter, self).get_context()
        context.update({
            'segments': BaseListPresenter(
                self.presented.segments(),
                title="Available Segments",
            )
        })
        return context


class SegmentPresenter(BasePresenter):

    templates_base_dir = 'segments/presenters/'
    template_presented_name = 'segment'

    def get_context(self):
        context = super(SegmentPresenter, self).get_context()
        context.update({
            'exercises': ExercisePresenter.from_list(
                self.presented.exercises()
            )
        })
        return context

    def edit_url(self):
        return reverse('workouts:edit_segment', kwargs={
            'workout_id': self.presented.workout.id,
            'segment_id': self.presented.id
        })
