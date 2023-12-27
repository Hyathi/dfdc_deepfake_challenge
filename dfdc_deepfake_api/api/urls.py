# api/urls.py
from django.urls import path
from .views import verifyVideoAPIView

urlpatterns = [
    path('verify/video', verifyVideoAPIView.as_view(), name='verify/video'),
]
