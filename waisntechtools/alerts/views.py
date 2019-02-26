from django.views.generic import ListView

from alerts.models import Subscriber


class DebugView(ListView):
    model = Subscriber
    template_name = 'alerts/debug.html'
    context_object_name = 'subscribers'

    def get_queryset(self):
        return Subscriber.objects.order_by('-date_registered')
