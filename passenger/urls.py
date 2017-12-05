from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^$',views.homeq,name='homepa'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^login_pass)
    url(r'^login/$', auth_views.login,{'template_name': 'login_pas.html'}, name='login'),


]