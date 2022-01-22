from django.urls import path  
from .views import HomePageView, ClientListCreateView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('clients/', ClientListCreateView.as_view(), name='clients-list-create'), 
    # # path('client/edit/<int:pk>', ClientEditView.as_view(), name='client-update'), 
    # path('products/', ProductListCreateView.as_view(), name='products-list-create'), 
    # path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client-delete'),
] 
