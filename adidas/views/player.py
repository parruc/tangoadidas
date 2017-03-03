from adidas.models import Player
from adidas.views.shortcuts import LoginRequiredMixin
from adidas.views.shortcuts import ProfileObjectMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView


class RankingView(ListView, LoginRequiredMixin):
    template_name = "adidas/ranking.html"
    model = Player
    queryset = Player.objects.annotate(points_sum=Sum('playerpointsinevent__points')).order_by('points_sum')


class ProfileUpdateView(ProfileObjectMixin, LoginRequiredMixin, UpdateView):
    """
    A view that displays a form for editing a user's profile.

    Uses a form dynamically created for the `Player` model and
    the default model's update template.
    """
    success_url = reverse_lazy("profile_view")
    fields = ["first_name", "last_name", "birth_date", "username", "image",
              "phone_number"]


class ProfileDetailView(ProfileObjectMixin, LoginRequiredMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
