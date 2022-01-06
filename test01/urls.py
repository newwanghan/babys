from django.urls import path
from .views import *

urlpatterns = [
    path('tmp', tmp, name='tmp'),
    path('tmp02', tmp02, name='tmp02'),
]
