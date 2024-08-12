from django.contrib import admin
from django.urls import path, include
from items import views as items_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', items_views.register, name='register'),
    path('', include('items.urls')),
]
