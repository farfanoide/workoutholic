# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.apps import AppConfig

class ExercisesConfig(AppConfig):

    name = 'exercises'

    def ready(self):
        """Import signal receivers."""
        # TODO: check why this is not being loaded
        from applications.exercises import receivers
