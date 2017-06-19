# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.conf.urls import url

from .views import *  # nopep8

urlpatterns = [

    url(r'^$', ListWorkoutsView.as_view(), name='index'),

]

