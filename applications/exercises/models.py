# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.db import models
from django.urls import reverse

from .presenters import ExercisePresenter


class Exercise(models.Model):

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    video = models.FileField(
        upload_to='exercises/videos/',
        storage=settings.DEFAULT_STORAGE
    )

    notes = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercises:show', kwargs={'exercise_id': self.id})

    def to_html(self):
        return ExercisePresenter(self).render()
