from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^r/$', views.RedditListView.as_view(), name='reddit'),
    url( r'^sd/$', views.SlashdotListView.as_view(), name='slashdot'),
    url( r'^hd/$', views.HackernewsListView.as_view(), name='hackernews'),
]



