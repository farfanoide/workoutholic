# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.db import models


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

