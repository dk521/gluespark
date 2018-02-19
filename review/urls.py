from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'gluespark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index, name = 'index' ),
    url(r'^signup$',views.signup, name = 'signup' ),
    url(r'^login$',views.login, name = 'login' ),
    url(r'^login/login_success$',views.login_success, name = 'login_successful' ),
    #url(r'^substore$',views.substore, name = 'substore' ),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
