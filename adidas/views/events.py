from adidas.forms import JoinEventForm
from adidas.models import Event
from adidas.views.shortcuts import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView


class EventsView(ListView):
    template_name = "adidas/events.html"
    model = Event
    queryset = Event.objects.order_by('start_date', 'start_time')

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_anonymous():
            return context
        team = self.request.user.team
        for event in context["event_list"]:
            event.is_my_team_allowed = event.is_my_teams_registred = False
            if team in event.allowed_teams.all():
                event.is_my_team_allowed = True
            if team in event.teams.all():
                event.is_my_teams_registred = True
        return context


class EventJoinView(FormView, LoginRequiredMixin):
    form_class = JoinEventForm
    success_url = reverse_lazy("events")

    def form_valid(self, form):
        event = form.cleaned_data.get('event', "")
        team = self.request.user.team
        if event and team:
            event.teams.add(team)
            event.save()
            messages.add_message(self.request, messages.INFO,
                                 'Hai iscritto la tua squadra all\'evento')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Non è stato possibile iscrivere la tua '
                                 'squadra all\'evento.')
        return redirect(reverse("events"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             'Non è stato possibile iscrivere la tua '
                             'squadra all\'evento.')
        return redirect(self.success_url)
