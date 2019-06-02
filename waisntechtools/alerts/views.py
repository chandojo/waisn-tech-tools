from django.shortcuts import render
from django.views.generic import ListView

from alerts.models import Subscriber
from alerts.waisn_auth import waisn_auth


@waisn_auth
def index(request):
    return render(request, 'alerts/index.html')


@waisn_auth
def debug(request):
    return DebugView.as_view()(request)


class DebugView(ListView):
    model = Subscriber
    template_name = 'alerts/debug.html'
    context_object_name = 'subscribers'

    def get_queryset(self):
        return Subscriber.objects.order_by('-date_registered')
