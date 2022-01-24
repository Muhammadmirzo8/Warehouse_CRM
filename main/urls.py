from django.urls import path  
from .views import HomePageView, StatsListCreateView, StatsUpdateView ,StatsDeleteView,  ClientListCreateView, ClientDeleteView, ClientUpdateView, ProductListCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    #clients
    path('clients/', ClientListCreateView.as_view(), name='clients-list-create'), 
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),  
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),

    #products 
    path('products/', ProductListCreateView.as_view(), name='products-list-create'), 
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product-update'), 
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'), 

    #stats 
    path('stats/', StatsListCreateView.as_view(), name='stats-list-create'), 
    path('stats/edit/<int:pk>/', StatsUpdateView.as_view(), name='stats-update'), 
    path('stats/delete/<int:pk>/', StatsDeleteView.as_view(), name='stats-delete'),
] 
