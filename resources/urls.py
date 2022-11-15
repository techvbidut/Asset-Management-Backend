from django.urls import path
from knox import views as knox_views
from .views import *

urlpatterns = [
    path('api/list-resources/', ListResources.as_view(), name='list-resources'),
]
