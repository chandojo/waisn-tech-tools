from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from alerts.models import Subscriber
from alerts.waisn_auth import waisn_auth
from alerts.debug_twilio import debug_twilio

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


class DebugView(TemplateView):
    template_name = 'alerts/debug.html'

    def get_twilio(self, **kwargs):
        return debug_twilio()

    def get_context_data(self, **kwargs):
        context = super(DebugView, self).get_context_data(**kwargs)
        context['messages'] = self.get_twilio
        context['subscribers'] = Subscriber.objects.order_by('-date_registered')
        return context
