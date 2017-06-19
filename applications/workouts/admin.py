# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.contrib import admin

from .models import *  # nopep8

admin.site.register(Workout)
admin.site.register(WorkoutType)
admin.site.register(Segment)
admin.site.register(SegmentExercise)
