# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Urls
from .utils import get_link, get_url_status
import gevent


class LinkStatuses(View):
    def get(self, request):
        urls = Urls.objects.all()

        jobs = [gevent.spawn(get_url_status, link) for link in urls]
        gevent.joinall(jobs)
        response = [dict(url=urls[n].url,
                         enabled=urls[n].enabled,
                         status=job.value) for n, job in enumerate(jobs)]

        ajax_request = request.GET.get('ajax_request', False)
        if ajax_request:
            return JsonResponse({'data': response})

        return render(request, 'links_status.html')

    def post(self, request):
        url = request.POST.get('url', None)
        if url:
            link = get_link(url)
            link.enabled = not link.enabled
            link.save()
            return JsonResponse({'status': 'ok'})

        return JsonResponse({'status': 'failed'})



