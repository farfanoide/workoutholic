# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django import forms

from djangoformsetjs.utils import formset_js_path

from applications.workouts.models import (
    Segment,
    SegmentExercise,
    Workout,
)
from applications.core.widgets import ComboDateInput

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('date', 'trainee', )
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

    class Media:
        js = (
            formset_js_path,
            'js/formset_input.js'
        )

    class Meta:
        model = SegmentExercise
        fields = ('segment', 'exercise', 'reps')
        widgets = {
            'segment': forms.HiddenInput
        }

SegmentExerciseFormSet = forms.modelformset_factory(
    SegmentExercise,
    form=SegmentExerciseForm,
    can_delete=True,
    min_num=1,
    validate_min=True,
    extra=0,
    fields=('exercise', 'reps')
)
