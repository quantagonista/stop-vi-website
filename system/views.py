# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.utils import translation

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'system/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_language = self.request.POST.get('lang')
            translation.activate(user_language)

        return render(request, self.template_name)
