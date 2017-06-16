# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
