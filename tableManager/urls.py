from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
path('store/update_store/<str:pk>/', views.updateStore, name="update_store"),
path('jewelry/update_jewelry/<str:pk>/', views.updateJewelry, name="update_jewelry"),
path('clients/create_client/', views.createClient, name="create_client"),
path('clients/update_client/<str:pk>/', views.updateClient, name="update_client"),
path('clients/delete_client/<str:pk>/', views.deleteClient, name="delete_client"),
path('jewelry/delete_jewelry/<str:pk>/', views.deleteJewelry, name="delete_jewelry"),
path('store/delete_store/<str:pk>/', views.deleteStore, name="delete_store"),
path('stores/create_store/', views.createStore, name="create_store"),
path('jewelry/create_jewelry/', views.createJewelry, name="create_jewelry"),
    path('clients/', views.clients, name='clients'),
    path('jewelry/', views.jewelry, name='jewelry'),
    path('stores/', views.stores, name='stores'),
    path('profile/', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', views.loginUser, name='login'),
path('logout', views.logoutUser, name='logout')
]