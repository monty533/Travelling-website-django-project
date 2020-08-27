from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index_view,name='Home'),
    path('register/',views.register_view,name='Register'),
    path('login/',views.login_view,name='Login'),
    path('logout/',views.logout_view,name='Logout'),
    path('about/',views.about_view,name='About'),
    path('cities/',views.cities_view,name='Cities'),
    

]
