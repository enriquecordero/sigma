from django.urls import path
from app_contact import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('app_info/<str:pk>/', views.app_info, name='app_info')
]