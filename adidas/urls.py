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
from adidas.views import HomepageView
from adidas.views import ProfileDetailView
from adidas.views import ProfileUpdateView
from adidas.views import RankingView
from adidas.views import TeamDetailView
from adidas.views import TeamJoinByHashView
from adidas.views import TeamJoinView
from adidas.views import TeamLeaveView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^accounts/profile/$', ProfileDetailView.as_view(),
        name="profile_view"),
    url(r'^profile/update/$', ProfileUpdateView.as_view(),
        name="profile_update"),
    url(r'^team/$', TeamDetailView.as_view(),
        name="team_view"),
    url(r'^team/join/$', TeamJoinView.as_view(),
        name="team_join"),
    url(r'^team/join/(?P<hash>\w+)/$', TeamJoinByHashView.as_view(),
        name="team_join_hash"),
    url(r'^team/leave/$', TeamLeaveView.as_view(),
        name="team_leave"),
    url(r'^ranking/$', RankingView.as_view(),
        name="ranking"),
]
