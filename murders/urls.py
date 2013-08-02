from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^murder', include('catalog.urls')),
        (r'^accounts/login/', 'django.contrib.auth.views.login',
            {'template_name': 'login.html'}),
        (r'^$', 'catalog.views.homepage'),
        (r'^roles$', 'roles.views.played'),
)
