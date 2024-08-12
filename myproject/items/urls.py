from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('item_list/', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('<int:pk>/edit/', views.item_update, name='item_update'),
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),
]
