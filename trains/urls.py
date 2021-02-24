from django.contrib import admin
from django.urls import path

from trains.views import *

urlpatterns = [
    path('', TrainListView.as_view(), name='home'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('edit/<int:pk>', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TrainDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
]

app_name = 'trains'