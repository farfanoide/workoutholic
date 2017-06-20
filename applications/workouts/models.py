# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.db import models
from django.urls import reverse

from applications.exercises.models import Exercise


class Workout(models.Model):

    date = models.DateField()

    def get_absolute_url(self):
        return reverse('workouts:show', kwargs={'workout_id': self.id})

    def to_html(self):
        return str(self.date)


class WorkoutType(models.Model):

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Segment(models.Model):

    workout = models.ForeignKey(Workout)

    workout_type = models.ForeignKey(WorkoutType)

    order = models.PositiveSmallIntegerField()

    notes = models.TextField()

    laps = models.PositiveSmallIntegerField(default=1)


class SegmentExercise(models.Model):

    segment = models.ForeignKey(Segment)

    exercise = models.ForeignKey(Exercise)

    reps = models.PositiveSmallIntegerField()
