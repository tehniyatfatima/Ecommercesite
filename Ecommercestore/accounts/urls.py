from django.urls import path


from .import views
from .views import signup_view, login_view
## for using direct logout functionality
##from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('accounttest/', views.accounttest, name='accounttest'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    # path("logout/", LogoutView.as_view(next_page ='login'), name= "logout"),
    
  
]