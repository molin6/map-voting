# example/urls.py
from django.urls import path

from example.views import index, map_view,submit_state

urlpatterns = [
    path('', index),
    path('map/', map_view, name='map'),
    path('submit_state/', submit_state, name='submit_state'),


]