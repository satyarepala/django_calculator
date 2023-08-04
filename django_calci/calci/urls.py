from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.basic_calculator_view, name='basic_calculator'),
    path('advanced/', views.advanced_calculator_view, name='advanced_calculator'),
]

