from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='index'),
    url(r'^home/$',views.home,name='homedr'),
    url(r'^setup/$',views.setup,name='profile_setup'),
    url(r'^create_profile',views.create_profile,name='create_profile'),
    url(r'^edit_profile',views.edit_profile,name='edit_profile')

]