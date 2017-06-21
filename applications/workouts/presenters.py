# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from applications.core.presenters import BasePresenter

__all__ = (
    'WorkoutPresenter',
)

class WorkoutPresenter(BasePresenter):

    templates_base_dir = 'workouts/presenters/'
    template_presented_name = 'workout'
    templates = {'show': 'show'}
