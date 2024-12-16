from django.urls import path
# from .views import test
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('', views.test, name='test'),
    path("", views.main_page, name="main_page"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/add/<int:pk>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("cart/add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("wishlist/remove/<int:pk>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path("logout/", LogoutView.as_view(next_page ='login'), name= "logout"),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)