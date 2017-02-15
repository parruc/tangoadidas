"""adidas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from allauth.account import views as auth_views
from allauth.socialaccount import views as socialauth_views
from allauth.socialaccount.providers.facebook import views as facebook_views
from django.conf.urls import url


urlpatterns = [
               #  url(r"^signup/$", auth_views.SignupView.as_view(),
               #       name='account_signup'),
               url(r"^login/$", auth_views.LoginView.as_view(),
                   name='account_login'),
               url(r"^logout/$", auth_views.LogoutView.as_view(),
                   name='account_logout'),
               #  url(r"^password/change/$",
               #      auth_views.PasswordChangeView.as_view(),
               #      name='account_change_password'),
               #  url(r"^password/set/$", auth_views.PasswordSetView.as_view(),
               #      name='account_set_password'),
               url(r"^inactive/$", auth_views.AccountInactiveView.as_view(),
                   name='account_inactive'),
               #  url(r"^email/$", auth_views.EmailView.as_view(),
               #      name='account_email'),
               #  url(r"^confirm-email/$",
               #      auth_views.EmailVerificationSentView.as_view(),
               #      name='account_email_verification_sent'),
               #  url(r"^confirm-email/(?P<key>[-:\w]+)/$",
               #     auth_views.ConfirmEmailView.as_view(),
               #     name='account_email_verification_sent'),
               #  url(r"^password/reset/$",
               #      auth_views.PasswordResetView.as_view(),
               #      name='account_reset_password'),
               #  url(r"^password/reset/done/$",
               #      auth_views.PasswordResetDoneView.as_view(),
               #      name='account_reset_password_done'),
               #  url(r"^password/reset/key/done/$",
               #      auth_views.PasswordResetFromKeyDoneView.as_view(),
               #      name='account_reset_password_from_key_done'),
               #  url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
               #      auth_views.PasswordResetFromKeyView.as_view(),
               #      name='account_reset_password_from_key'),
               url(r"^social/login/cancelled/$",
                   socialauth_views.LoginCancelledView.as_view(),
                   name='socialaccount_login_cancelled'),
               url(r"^social/login/error/$",
                   socialauth_views.LoginErrorView.as_view(),
                   name='socialaccount_login_error'),
               url(r"^social/signup/$", socialauth_views.SignupView.as_view(),
                   name='socialaccount_signup'),
               url(r"^social/connections/$",
                   socialauth_views.ConnectionsView.as_view(),
                   name='socialaccount_connections'),
               url(r"^facebook/login/$", facebook_views.oauth2_login,
                   name='facebook_login'),
               url(r"^facebook/login/callback/$",
                   facebook_views.oauth2_callback,
                   name='facebook_callback'),
               url(r"^facebook/login/token/$", facebook_views.login_by_token,
                   name='facebook_login_by_token'),
               url(r"^instagram/login/$", facebook_views.login_by_token,
                   name='instagram_login'),
               url(r"^instagram/login/callback/$",
                   facebook_views.login_by_token, name='instagram_callback'),
               ]
