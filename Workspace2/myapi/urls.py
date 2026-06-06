from django.urls import path
from .views import get_users,create_user  # Import your views here

urlpatterns = [
    # Route for your function view
    path('user/<int:pk>', get_users, name='get-users'),
    path('user/create/', create_user, name='create-user'),
]