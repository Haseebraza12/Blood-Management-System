from django.urls import path
from django.contrib.auth.views import LoginView
from . import views as ngo_views  # Alias to avoid conflicts with other views

urlpatterns = [
    path('donorlogin/', LoginView.as_view(template_name='ngo/donorlogin.html'), name='donorlogin'),
    path('donorsignup/ngologin/', LoginView.as_view(template_name='ngo/donorlogin.html'), name='ngologin'),
    path('donorsignup/', ngo_views.ngo_signup_view, name='ngosignup'),
    path('donor-dashboard/', ngo_views.ngo_dashboard_view, name='ngo-dashboard'),
    path('donate-blood/', ngo_views.ngo_blood_view, name='donate-blood'),
    path('donation-history/', ngo_views.donation_history_view, name='donation-history'),
    path('make-request/', ngo_views.make_request_view, name='make-request'),
    path('make-request/request-history/request-history/',ngo_views.make_request_view, name='make-request'),
    path('make-request/request-history/',ngo_views.make_request_view, name='make-request'),
    path('request-history/', ngo_views.request_history_view, name='request-history'),
]
