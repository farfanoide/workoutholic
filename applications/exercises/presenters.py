# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from applications.core.presenters import BasePresenter

__all__ = (
    'ExercisePresenter',
)

class ExercisePresenter(BasePresenter):

    templates_base_dir = 'exercises/presenters/'
    template_presented_name = 'exercise'
    templates = {'show': 'show'}
