from django.urls import path
from . import views

urlpatterns = [
    path('function', views.function_based_view),
    path('class', views.ClassBasedView.as_view()),
]