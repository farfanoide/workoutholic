# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='workouts/home.html')),

    url(r'^exercises/',
        include('applications.exercises.urls', namespace='exercises')),

    url(r'^workouts/',
        include('applications.workouts.urls', namespace='workouts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
