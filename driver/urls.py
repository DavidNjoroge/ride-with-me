from django.conf.urls import url,include
from . import views
app_name='driver'
urlpatterns=[
    url(r'^$',views.home,name='index'),
    url(r'^home/$',views.home,name='homedr'),
    url(r'^setup/$',views.setup,name='profile_setup'),
    url(r'^create_profile',views.create_profile,name='create_profile'),
    url(r'^edit_profile/',views.edit_profile,name='edit_profile'),
    url(r'^edit_location/',views.edit_location,name='edit_location'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^ajax/locale/$',views.ajax_locale,name='ajax_locale'),

] 