from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^siteAlcione/Site', include('Site.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': '/var/www/pjtAptana/siteAlcione/media/'}),
)
