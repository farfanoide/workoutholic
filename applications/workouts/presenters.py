# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from applications.core.presenters import BasePresenter, BaseListPresenter

__all__ = (
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
