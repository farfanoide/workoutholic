# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django import forms

from applications.workouts.models import Workout
from applications.core.widgets import ComboDateInput

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('date',)
        widgets = {
            'date': ComboDateInput
        }
