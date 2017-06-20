# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django import forms

from applications.workouts.models import (
    Segment,
    SegmentExercise,
    Workout,
)
from applications.core.widgets import ComboDateInput

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('date',)
        widgets = {'date': ComboDateInput}


class SegmentForm(forms.ModelForm):

    class Meta:
        model = Segment
        fields = (
            'laps',
            'notes',
            'order',
            'workout',
            'workout_type',
        )
        widgets = {'workout': forms.HiddenInput}

class SegmentExerciseForm(forms.ModelForm):

    class Meta:
        model = SegmentExercise
        fields = ('segment', 'exercise', 'reps')
