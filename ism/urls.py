from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'ism.views.home', name='home'),
#     url(r'^movie/', include('movie.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
