from django.conf.urls import patterns, include, url
from api import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forage.views.home', name='home'),
    # url(r'^forage/', include('forage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url()
    url(r'merge', views.merge_restaurants ),
    url(r'scrape_google', views.scrape_google ),
    url(r'scrapegrid',views.scrape_grid_page ),
    url(r'scrape',views.scrape ),
    url(r'locate', views.locate ),

)
