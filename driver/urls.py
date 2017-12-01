from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^setup/$',views.setup,name='profile_setup')
]