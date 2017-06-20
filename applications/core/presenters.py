# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.template import loader

class BasePresenter(object):

    templates_base_dir = 'core/presenters/'
    template_presented_name = 'object'
    templates_suffix = '.html'

    # TODO: use better name for presented
    def __init__(self, presented):
        self.presented = presented

    def get_template(self, template_name='show'):
        template_name = "{base_dir}{template}{suffix}".format(
            base_dir=self.templates_base_dir,
            template=self.templates[template_name],
            suffix=self.templates_suffix)
        return loader.get_template(template_name)

    def get_context(self):
        raise NotImplementedError()

    def render(self):
        return self.get_template().render(self.get_context())

    def get_context(self):
        return {self.template_presented_name: self.presented}
