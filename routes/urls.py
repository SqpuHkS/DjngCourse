from django.urls import path

from routes.views import *

urlpatterns = [
    path('find_routes/', find_routes, name='find'),
    path('add_route/', add_route, name='add'),
    path('save_route/', save_route, name='save'),
    path('list/', RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
    path('', home, name='home'),
]
