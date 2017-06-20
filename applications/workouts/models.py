# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.db import models
from django.urls import reverse

from applications.exercises.models import Exercise
from applications.workouts.presenters import WorkoutPresenter


class Workout(models.Model):

    date = models.DateField()

    def get_absolute_url(self):
        return reverse('workouts:show', kwargs={'workout_id': self.id})

    def to_html(self):
        return WorkoutPresenter(self).render()

    def __str__(self):
        return str(self.date)

    def segments(self):
        return self.segment_set.all()


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

    def get_absolute_url(self):
        return reverse('workouts:show', kwargs={'workout_id': self.workout.id})

    def exercises(self):
        # TODO: Refactor to use queryset instead of list comprehension
        return [se.exercise for se in self.segmentexercise_set.all()]

class SegmentExercise(models.Model):

    segment = models.ForeignKey(Segment)

    exercise = models.ForeignKey(Exercise)

    reps = models.PositiveSmallIntegerField()
