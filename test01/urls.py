from django.urls import path
from .views import *

urlpatterns = [
    path('tmp', tmp, name='tmp'),
]
