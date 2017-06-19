# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver

from applications.exercises.models import Exercise

@receiver(signals.post_delete, sender=Exercise)
def auto_delete_files(sender, instance, **kwargs):
    # TODO: check why this is not being loaded
    if bool(instance.video):
        settings.DEFAULT_STORAGE.delete(instance.video)
