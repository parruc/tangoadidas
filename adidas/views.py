# from django.shortcuts import render
#from django.urls import reverse
from adidas.models import Player
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView


class HomepageView(TemplateView):
    template_name = "adidas/homepage.html"


class TeamView(ListView):
    template_name = "adidas/team.html"
    model = Player

    def get_queryset(self):
        """Return's the current user team players."""
        import ipdb; ipdb.set_trace()
        return self.request.user.team.player_set.all()


class RankingView(ListView):
    template_name = "adidas/ranking.html"
    model = Player
    queryset = Player.objects.order_by('-points')


class ProfileObjMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Player

    def get_object(self):
        """Return's the current users profile."""
        return self.request.user

    @method_decorator(login_required(login_url=reverse_lazy('account_login')))
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileObjMixin, self).dispatch(request, *args, **kwargs)


class ProfileUpdateView(ProfileObjMixin, UpdateView):
    """
    A view that displays a form for editing a user's profile.

    Uses a form dynamically created for the `Player` model and
    the default model's update template.
    """
    success_url = reverse_lazy("profile_view")
    fields = ["first_name", "last_name", "birth_date", "username", "image",
              "phone_number"]


class ProfileDetailView(ProfileObjMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
