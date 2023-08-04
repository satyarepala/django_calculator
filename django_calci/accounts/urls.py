from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('signout/', views.user_login, name='signout'),
    path('', views.dashboard, name='dashboard'),
]
