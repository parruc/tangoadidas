from adidas.forms import JoinWithdrawEventForm
from adidas.models import Event
from adidas.views.mixins import CaptainRequiredMixin
from adidas.views.mixins import LoginRequiredMixin
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
            is_my_team_allowed = is_my_teams_registred = False
            if team in event.allowed_teams.all():
                is_my_team_allowed = True
            if team in event.teams.all():
                is_my_teams_registred = True
            if is_my_team_allowed and not is_my_teams_registred:
                event.can_join = True
            if is_my_team_allowed and is_my_teams_registred:
                event.can_witwdraw = True
            form = JoinWithdrawEventForm(initial={'hash': event.hash})
            event.joinwithdraw_event_form = form
        return context


class EventJoinWithdrawView(LoginRequiredMixin, CaptainRequiredMixin, FormView):
    form_class = JoinWithdrawEventForm
    success_url = reverse_lazy("events")
    ok_message = "Hai {action} la tua squadra all\'evento {title}."
    ko_message = "Non è stato possibile {action} la tua squadra all'evento {title}."

    def dispatch(self, request, *args, **kwargs):
        self.action = self.kwargs.get('action', "")
        if self.action == "join":
            self.ok_action = "iscritto"
            self.ko_action = "iscrivere"
        if self.action == "withdraw":
            self.ok_action = "disiscritto"
            self.ko_action = "disiscrivere"
        return super(EventJoinWithdrawView, self).dispatch(request,
                                                           *args, **kwargs)

    def form_valid(self, form):
        hash = form.cleaned_data.get('hash', "")
        event = Event.objects.filter(hash=hash).first()
        team = self.request.user.team
        if event and team:
            if self.action == "join":
                event.teams.add(team)
            elif self.action == "withdraw":
                event.teams.remove(team)
            event.save()
            messages.add_message(self.request, messages.INFO,
                                 self.ok_message.format(title=event.title,
                                                        action=self.ok_action))
        else:
            messages.add_message(self.request, messages.ERROR,
                                 self.ko_message.format(title=event.title,
                                                        action=self.ko_action))
        return redirect(reverse("events"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             self.ko_message.format(title="",
                                                    action=self.ko_action))
        return redirect(self.success_url)
