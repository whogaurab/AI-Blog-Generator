from django.urls import path
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1903953253.
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout')
]