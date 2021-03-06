from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from registration.backends.simple.views import RegistrationView


urlpatterns=[
    url(r'^$',views.homeq,name='homepa'),
    url(r'^setup/$',views.setup,name='profile_setup'),
    url(r'^login/$', auth_views.login,{'template_name': 'login_pas.html'}, name='login'),
    url(r'^register/$',RegistrationView.as_view(),{'template_name': '/registration/registration_for.html'},name='registration_register'),
    url(r'^setup/$',views.setup,name='profile_setup'),
    url(r'^edit_profile/$',views.edit_profile,name='passenger_edit_profile'),
    url(r'^ajax/locale/$',views.ajax_locale,name='ajax_locale'),
    url(r'^ajax/drivers/$',views.ajax_driver,name='ajax_drivers'),
    url(r'^driver/$',views.drivers,name='drivers'),
    url(r'^bookings/(\d+)',views.drivers),
    url(r'^book/(\d+)',views.book)
    
]