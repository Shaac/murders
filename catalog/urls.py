from django.conf.urls import patterns, url

urlpatterns = patterns('',
        (r'^s$', 'catalog.views.homepage'),
        (r'^-(?P<murder_id>\d+)$', 'catalog.views.murder'),
        (r'^-(?P<murder_id>\d+)-([\w\-]*)$', 'catalog.views.murder'),
)
