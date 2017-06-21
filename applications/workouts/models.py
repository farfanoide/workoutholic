# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.db import models
from django.urls import reverse

from applications.exercises.models import Exercise
from applications.workouts.presenters import WorkoutPresenter


class Workout(models.Model):

    date = models.DateField()

    trainee = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return "Workout for {user} on {date}".format(
            user=self.trainee, date=self.date
        )

    def __repr__(self):
        return '<{string_repr}>'.format(string_repr=self.__str__())

    def get_absolute_url(self):
        return reverse('workouts:show', kwargs={'workout_id': self.id})

    def to_html(self):
        return WorkoutPresenter(self).render()

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
        return Exercise.objects.filter(segmentexercise__segment=self)


class SegmentExercise(models.Model):

    segment = models.ForeignKey(Segment)

    exercise = models.ForeignKey(Exercise)

    reps = models.PositiveSmallIntegerField()
