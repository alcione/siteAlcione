from django.conf.urls import patterns, include, url
from Site.views import home
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siteAlcione.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^$/', home)
   
   )
