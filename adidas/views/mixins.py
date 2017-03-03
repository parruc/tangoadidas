from adidas.models import Player
from adidas.models import Team
from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin


class LoginRequiredMixin(BaseLoginRequiredMixin):
    login_url = reverse_lazy('account_login')


class PlayerObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Player

    def get_object(self):
        """Return's the current users profile."""
        return self.request.user


class TeamObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Team

    def get_object(self):
        """Return's the current users profile."""
        return getattr(self.request.user, "team", None)
