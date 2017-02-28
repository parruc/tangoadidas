from adidas.models import Player
from django.contrib.auth.mixins import LoginRequiredMixin as BLoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin


class LoginRequiredMixin(BLoginRequiredMixin):
    login_url = reverse_lazy('account_login')


class ProfileObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Player

    def get_object(self):
        """Return's the current users profile."""
        return self.request.user
