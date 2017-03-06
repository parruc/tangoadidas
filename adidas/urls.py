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
from adidas.views.events import EventJoinWithdrawView
from adidas.views.events import EventsView
from adidas.views.generic import HomepageView
from adidas.views.player import ProfileDetailView
from adidas.views.player import ProfileUpdateView
from adidas.views.player import RankingView
from adidas.views.team import TeamDetailView
from adidas.views.team import TeamJoinByHashView
from adidas.views.team import TeamJoinView
from adidas.views.team import TeamLeaveView
from adidas.views.team import TeamRemoveView
from adidas.views.team import TeamUpdateView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^accounts/profile/$', ProfileDetailView.as_view(),
        name="profile_view"),
    url(r'^profile/update/$', ProfileUpdateView.as_view(),
        name="profile_update"),
    url(r'^team/$', TeamDetailView.as_view(),
        name="team_view"),
    url(r'^team/update/$', TeamUpdateView.as_view(),
        name="team_update"),
    url(r'^team/join/$', TeamJoinView.as_view(),
        name="team_join"),
    url(r'^team/remove/$', TeamRemoveView.as_view(),
        name="team_remove"),
    url(r'^team/join/(?P<hash>\w+)/$', TeamJoinByHashView.as_view(),
        name="team_join_hash"),
    url(r'^team/leave/$', TeamLeaveView.as_view(),
        name="team_leave"),
    url(r'^ranking/$', RankingView.as_view(),
        name="ranking"),
    url(r'^events/$', EventsView.as_view(),
        name="events"),
    url(r'^event/(?P<action>(join|withdraw))/$', EventJoinWithdrawView.as_view(),
        name="event_join_withdraw"),
]
