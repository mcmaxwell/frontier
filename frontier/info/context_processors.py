from info.models import Info, MenuLinks
from django.core.context_processors import request

def info(request):
    info = Info.objects.all()
    return {"info": info}

def links(request):
    links = MenuLinks.objects.all()
    return {"links": links}
