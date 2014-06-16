from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oauthwork.views.home', name='home'),
    # url(r'^oauthwork/', include('oauthwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', index, name='home'),
    url(r'^welcome/', welcome, name='welcome'),
    url(r'^logout/', logout, name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social'))

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
