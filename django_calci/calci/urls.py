from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.basic_calculator_view, name='basic_calculator'),
    path('advanced/', views.advanced_calculator_view, name='advanced_calculator'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback')
]




