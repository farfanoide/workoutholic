# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.template import loader

__all__ = (
    'ExercisePresenter',
)

class ExercisePresenter(object):

    templates_base_dir = 'exercises/presenters/'
    templates_suffix = '.html'
    templates = {
        'show': 'show'
    }

    def get_template(self, template_name='show'):
        template_name = "{base_dir}{template}{suffix}".format(
            base_dir=self.templates_base_dir,
            template=self.templates[template_name],
            suffix=self.templates_suffix)
        return loader.get_template(template_name)

    def __init__(self, exercise):
        self.exercise = exercise

    def get_context(self):
        return {'exercise': self.exercise}

    def render(self):
        return self.get_template().render(self.get_context())
