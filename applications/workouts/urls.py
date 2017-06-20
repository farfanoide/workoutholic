# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.conf.urls import url

from .views import *  # nopep8

urlpatterns = [

    url(r'^$', ListWorkoutsView.as_view(), name='index'),

    url(r'^create$', CreateWorkoutView.as_view(), name='create'),

    url(r'^(?P<workout_id>\d+)$', ShowWorkoutView.as_view(), name='show'),

    url(r'^(?P<workout_id>\d+)/add_segment$',
        AddSegmentView.as_view(),
        name='add_segment'),

    url(r'^(?P<workout_id>\d+)/segment/(?P<segment_id>\d+)$',
        ShowSegmentView.as_view(),
        name='show_segment'),


]

