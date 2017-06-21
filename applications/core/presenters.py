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

    def get_template_name(self, name='show'):
        template_name =  "{base_dir}{template}{suffix}".format(
            base_dir=self.templates_base_dir,
            template=self.templates[name],
            suffix=self.templates_suffix
        )
        return template_name

    def get_template(self):
        return loader.get_template(self.get_template_name())

    def render(self):
        return self.get_template().render(self.get_context())

    def get_context(self):
        return {self.template_presented_name: self.presented}

    def __str__(self):
        return self.render()

class BaseListPresenter(BasePresenter):

    templates_base_dir = 'generic/presenters/'
    template_presented_name = 'queryset'
    templates = {'show': 'list'}

    def __init__(self, presented, title=None):
        self.presented = presented
        self.title = title

    def get_context(self):
        context = super(BaseListPresenter, self).get_context()
        context.update({'title': self.title})
        return context
