from django.conf.urls import patterns, include, url

from django.contrib import admin
from bbblog import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'bbblog.views.hello'),
    url(r'^time/$', 'bbblog.views.current_datetime'),
    url(r'^meta/$', 'bbblog.views.display_meta'),
    url(r'^searchform/$', 'books.views.search_form'),
    url(r'^search/$', 'books.views.search'),
    )
