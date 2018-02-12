from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class NewsListView(TemplateView):

    template_name = "news/news_list.html"

    def get_context_data(self, **kwargs):
        first_news = News.objects.all().order_by('-publication_date', '-id').first()
        if first_news.image:
           news = News.objects.all().order_by('-publication_date', '-id')[:8]
        else:
           news = News.objects.all().order_by('-publication_date', '-id')[:9]
        news_list = News.objects.all()
        print len(news_list)

        if len(news_list) > 9:
            more_status = True
            print "Hello"
        else:
            more_status = False

        context = super(NewsListView, self).get_context_data(**kwargs)
        context['more_status'] = more_status
        context['news'] = news
        return context



class NewsView(DetailView):
    model = News
    #template_name = 'agenda/agenda_gallery.html'


    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        active_news = News.objects.get(slug=self.kwargs.get('slug'))

        context = super(NewsView, self).get_context_data(**kwargs)
        #context["images"] = NewsImage.objects.filter(news_id=int(active_news.id))
        return context


def news_updater(request):

    #news_quantity = 8

    if request.method == 'GET':
        news = News.objects.all().order_by('-publication_date', '-id')
        return render(request, 'news/news_index_dynamic.html', {'news': news})
