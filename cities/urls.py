from django.contrib import admin
from django.urls import path

from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('edit/<int:pk>', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CityDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),

]
