from django.shortcuts import render

# Create your views here. 
#encoding: utf-8


from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.sites.models import Site
from .forms import SiteForm


def home(request):
    
    form = SiteForm()
    site = Site.objects.all()
    mi_template = loader.get_template("home.html")
    mi_contexto = Context({'site':site})
    return HttpResponse(mi_template.render(mi_contexto))