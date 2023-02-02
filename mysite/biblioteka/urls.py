from django.urls import path
from . import views

urlpatterns = [
    path('', views.pradzia, name='pradzia'),
    path('autoriai/', views.AutoriaiListView.as_view(), name='autoriai'),
    path('knygos/', views.KnygosListView.as_view(), name='knygos'),
    path('knygos/<int:pk>', views.KnygosDetailView.as_view(), name='knyga')
]