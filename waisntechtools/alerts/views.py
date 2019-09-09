from django.shortcuts import render
from django.views.generic import ListView

from alerts.models import Subscriber
from alerts.waisn_auth import waisn_auth
from alerts.fetch_twilio import fetch_twilio

import requests

def get_post_request(get_handler, post_handler):
    def _handle_request(request):
        if request.method == 'POST':
            return post_handler(request)
        else:
            return get_handler(request)

    return _handle_request


@waisn_auth
def index(request):
    return render(request, 'alerts/index.html')


@waisn_auth
def debug(request):
    return DebugView.as_view()(request)


class DebugView(ListView):
    template_name = 'alerts/debug.html'
    context_object_name = 'subscribers'
    queryset = Subscriber.objects.order_by('-date_registered')

    def get_twilio(self, request, **kwargs):
        return fetch_twilio(request)

    def get_context_data(self, **kwargs):
        context = super(DebugView, self).get_context_data(**kwargs)
        context['messages'] = self.get_twilio
        return context
