from django.urls import path
from .views import MultipleModelAPIView 

urlpatterns = [
    path('vehicles/', MultipleModelAPIView.as_view(),name='vehicles'),
]