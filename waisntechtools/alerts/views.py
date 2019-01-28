from django.views import generic


class IndexView(generic.base.TemplateView):
    template_name = 'alerts/index.html'
