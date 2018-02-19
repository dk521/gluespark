from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gluespark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gluespark.com/', include('review.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
