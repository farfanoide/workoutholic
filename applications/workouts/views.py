# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.views.generic import (
    ListView,
)

from applications.workouts.models import Workout

__all__ = (
    'ListWorkoutsView',
)
#
#
class ListWorkoutsView(ListView):

    model = Workout
    template_name = 'workouts/list.html'
    context_object_name = 'workouts'
