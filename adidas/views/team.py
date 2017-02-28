from adidas.forms import JoinTeamForm
from adidas.models import Player
from adidas.models import Team
from adidas.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView


class TeamLeaveView(View, LoginRequiredMixin):
    success_url = reverse_lazy("team_view")

    def dispatch(self, *args, **kwargs):
        self.request.user.team = None
        self.request.user.save()
        messages.add_message(self.request, messages.INFO,
                             'Hai abbandonato la squadra')
        return redirect(self.success_url)


class TeamDetailView(ListView, LoginRequiredMixin):
    template_name = "adidas/team.html"
    model = Player

    def get_queryset(self):
        """Return's the current user team players."""
        if not self.request.user.team:
            return Player.objects.none()
        return self.request.user.team.player_set.all()

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context["join_team_form"] = JoinTeamForm()
        return context


class TeamJoinByHashView(View, LoginRequiredMixin):
    success_url = reverse_lazy("team_view")

    def dispatch(self, *args, **kwargs):
        hash = self.kwargs.get('hash', "")
        team = Team.objects.filter(hash=hash).first()
        if team:
            player = self.request.user
            player.team = team
            player.save()
            messages.add_message(self.request, messages.INFO,
                                 'Ti sei unito alla squadra')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Non è possibile aggiungerti alla squadra.\
                                 Verifica il codice inserito.')
        return redirect(self.success_url)


class TeamJoinView(FormView, LoginRequiredMixin):
    form_class = JoinTeamForm
    success_url = reverse_lazy("team_view")

    def form_valid(self, form):
        hash = form.cleaned_data.get('hash', "")
        team = Team.objects.filter(hash=hash).first()
        if team:
            player = self.request.user
            player.team = team
            player.save()
            messages.add_message(self.request, messages.INFO,
                                 'Ti sei unito alla squadra')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'Non è possibile aggiungerti alla squadra.\
                                 Verifica il codice inserito.')
        return redirect(reverse("team_view"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             'Non hai inserito un codice valido')
        return redirect(self.success_url)
