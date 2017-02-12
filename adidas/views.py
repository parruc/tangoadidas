# from django.views.generic.edit import DeleteView
# from django.shortcuts import render
#from django.urls import reverse
from adidas.models import Player
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


class HomepageView(TemplateView):
    template_name = "adidas/homepage.html"


class ProfileObjMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = Player

    def get_object(self):
        """Return's the current users profile."""
        try:
            return self.request.user.player
        except Player.DoesNotExist:
            raise NotImplemented(
                "What if the user doesn't have an associated profile?")

    @method_decorator(login_required(login_url=reverse_lazy('sign-in')))
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileObjMixin, self).dispatch(request, *args, **kwargs)


class ProfileAddView(ProfileObjMixin, CreateView):
    """
    A view that creating a user's profile.

    Uses a form dynamically created for the `Player` model and
    the default model's update template.
    """
    pass


class ProfileUpdateView(ProfileObjMixin, UpdateView):
    """
    A view that displays a form for editing a user's profile.

    Uses a form dynamically created for the `Player` model and
    the default model's update template.
    """
    pass


class ProfileDetailView(ProfileObjMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['memberships'] = context["player"].teammembership_set.all()
        return context


class RegistrationView(TemplateView):
        template = "adidas/homepage.html"


class SignInView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = reverse_lazy('profile_view')
    form_class = AuthenticationForm
    redirect_fieldname = REDIRECT_FIELD_NAME
    template_name = "adidas/signin.html"

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(SignInView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(SignInView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_fieldname)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class SignOutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('homepage')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)
