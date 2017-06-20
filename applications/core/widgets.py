# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from django.forms.widgets import DateInput

class ComboDateInput(DateInput):

    class Media:
        js = (
            'moment/min/moment.min.js',
            'combodate/src/combodate.js',
            'js/combodate_input.js',
        )

    def __init__(self, attrs={}):
        format = ('%d/%m/%Y')
        attrs.update({
            'class': attrs.get('class', '') + ' combodate',
            'data-format': attrs.get('data-format', 'DD/MM/YYYY'),
            'data-template': attrs.get('data-template', 'D MMMM YYYY')
        })
        super(ComboDateInput, self).__init__(attrs, format)

