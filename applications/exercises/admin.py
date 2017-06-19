# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.contrib import admin

from applications.exercises.models import Exercise

admin.site.register(Exercise)
