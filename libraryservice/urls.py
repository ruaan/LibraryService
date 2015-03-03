from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.api import book_router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libraryservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v1/', include(book_router.urls)),
    url(r'^api-explorer/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
