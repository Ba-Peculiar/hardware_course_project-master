from django.urls import path
from .views import TemperatureDetailView,  TemperatureListView, TemperatureCreateAPIView, relay_control_view
from . import views

urlpatterns = [
    path('temperatures/', TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureDetailView.as_view(), name='temperature-detail'),
    path('temperature/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/get-readings/', views.get_readings, name='get_readings'),
    path('getrelaystatus/', views.get_relay_status, name='get_relay_status'),
    path('relay/control/', relay_control_view, name='relay_control'),

]
