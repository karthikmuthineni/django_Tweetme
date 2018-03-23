from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
	UserDetailView,
	UserFollowView

	)

urlpatterns = [

	url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/follow/$', UserFollowView.as_view(), name='follow/'),

]