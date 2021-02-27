from django.urls import path

from routes.views import *

urlpatterns = [
    path('find_routes/', find_routes, name='find_routes'),
    path('', home, name='home'),
]
