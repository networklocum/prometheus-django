# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.http import HttpResponse
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST


def metrics(request):
    if "prometheus_multiproc_dir" in os.environ:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        data = generate_latest(registry)
        return HttpResponse(data, content_type=CONTENT_TYPE_LATEST)
    return HttpResponse("")
