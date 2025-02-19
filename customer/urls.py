from django.urls import path
from .views import register, profile, login_view, logout_view

urlpatterns = [
    path('register/', register, name='customer_register'),
    path('profile/', profile, name='customer_profile'),
    path('login/', login_view, name='customer_login'),
    path('logout/', logout_view, name='customer_logout'),
]
