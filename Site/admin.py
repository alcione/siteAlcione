# -*- coding: utf-8 -*-
from .models import Site

from django.contrib import admin

class SiteAdmin(admin.ModelAdmin):
    model = Site
    list_display = ['titulo','descricao','imagem','link','email','status','data_cadastro']
    list_filter = ['status']
    search_fields = ['titulo']
    save_on_top = True
admin.site.register(Site, SiteAdmin)

