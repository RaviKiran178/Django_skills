from django.urls import path
from . import views

urlpatterns = [
    path('features/', views.index, name='feature'),
]