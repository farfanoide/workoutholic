# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.db import models

from applications.exercises.models import Exercise


class Routine(models.Model):

    date = models.DateField()


class WorkoutType(models.Model):

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )


class Segment(models.Model):

    routine = models.ForeignKey(Routine)

    workout_type = models.ForeignKey(WorkoutType)

    order = models.PositiveSmallIntegerField()

    notes = models.TextField()

    laps = models.PositiveSmallIntegerField(default=1)


class SegmentExercise(models.Model):

    segment = models.ForeignKey(Segment)

    exercise = models.ForeignKey(Exercise)

    reps = models.PositiveSmallIntegerField()
