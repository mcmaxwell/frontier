from django.conf.urls import include, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from news.models import News
from .views import NewsView, NewsListView, news_updater


urlpatterns = [
    url(r'^$',NewsListView.as_view()
        , name='news_list'),
    url(r'^(?P<slug>[^/]+)/$', NewsView.as_view()
        , name='news_detail'),
    url(r'^updater/result/', news_updater
        , name='news_updater'),

]
