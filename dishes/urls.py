from django.urls import path

from .views import index

app_name = 'dishes'

urlpatterns = [
    path('', index, name='index'),
]