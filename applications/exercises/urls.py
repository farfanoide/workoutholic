# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.conf.urls import url

from .views import *  # nopep8

urlpatterns = [

    url(r'^$', ListExercisesView.as_view(), name='index'),

    url(r'^create$', CreateExerciseView.as_view(), name='create'),

    url(r'^(?P<exercise_id>\d+)$', ShowExerciseView.as_view(), name='show'),

]
