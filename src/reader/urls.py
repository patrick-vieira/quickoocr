from django.urls import path

from .views import home, read, save, search, search_view

urlpatterns = [
    path('', home, name='home'),
    path('read', read, name='read'),
    path('save', save, name='save')
]

urlpatterns += [
    path('search', search, name='search'),
    path('search_view', search_view, name='search_view'),
]