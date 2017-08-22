# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    page_title = "Home"
    context = {
        "page_title": page_title,
    }
    return render(request, 'caring4us/index.html', context)
