from django.urls import path

from . import views

app_name = 'restaurants'

urlpatterns = [
    path(
        '',
        views.RestaurantListView.as_view(),
        name='restaurant_list'),
    path(
        'add-new-restaurant/',
        views.RestaurantCreateView.as_view(),
        name='restaurant_create'),
    path(
        '<slug:restaurant_slug>/',
        views.RestaurantDetailView.as_view(),
        name='restaurant_detail'),
    ]
