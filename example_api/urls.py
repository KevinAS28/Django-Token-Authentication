app_name = 'example_api'

from django.urls import path
from .views import *


urlpatterns = [
    path('helloworld', helloworld)
]