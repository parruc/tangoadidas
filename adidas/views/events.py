from adidas.models import Event
from django.views.generic import ListView


class EventsView(ListView):
    template_name = "adidas/events.html"
    model = Event
    queryset = Event.objects.order_by('start_date', 'start_time')
