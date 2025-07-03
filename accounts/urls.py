from django.urls import path 
from . import views
from .views import UserRegistrationView,UserLoginView,Profile
urlpatterns = [
    path('profile/',Profile.as_view(),name='profile'),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView,name='logout'),
]
