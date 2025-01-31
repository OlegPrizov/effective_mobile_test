from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dishes.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('users.urls')),
    path('api/', include('api.urls')),
]