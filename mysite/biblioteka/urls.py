from django.urls import path
from . import views

urlpatterns = [
    path('', views.pradzia, name='pradzia')
]