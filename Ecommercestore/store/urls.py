from django.urls import path
# from .views import test
from . import views

urlpatterns = [
    path('', views.test, name='test'),
  
]