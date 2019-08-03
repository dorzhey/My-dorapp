from django.urls import path
from . import views


urlpatterns = [
    path('', views.tool_list, name='tool_list'),
]
