from django.urls import path
from .views import ULoginView, RegisterUserView, CreateWareView
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', ULoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('ware/create/', CreateWareView.as_view(), name='ware-create'),
] 
