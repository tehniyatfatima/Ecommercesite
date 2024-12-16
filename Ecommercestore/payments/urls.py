from django.urls import path
# from .views import test
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    
    ##path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('payment-success/', views.payment_success, name='payment_success'),
]