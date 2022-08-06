from django.urls import path

from .views import home, read

urlpatterns = [
    path('', home, name='home'),
    path('read', read, name='read'),
]
