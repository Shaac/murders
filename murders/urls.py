from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^$', 'catalog.views.homepage'),
        (r'^murder-(?P<murder_id>\d+)$', 'catalog.views.murder'),
        (r'^murder-(?P<murder_id>\d+)-([\w\-]*)$', 'catalog.views.murder'),
)
