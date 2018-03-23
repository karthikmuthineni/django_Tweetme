from django.conf.urls import url

from .views import (
	tweet_detail_view, tweet_list_view, tweet_create_view
	)

urlpatterns = [
	#url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^$', tweet_list_view, name='list'),
    url(r'^create$', tweet_create_view, name='create'),
    url(r'^(?P<pk>\d+)1/$', tweet_detail_view, name='detail'),
    



]