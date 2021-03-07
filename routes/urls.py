from django.urls import path

from routes.views import *

urlpatterns = [
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('', home, name='home'),
]
