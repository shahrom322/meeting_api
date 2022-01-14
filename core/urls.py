from django.urls import path

from core.views import CreateUserAPIView

urlpatterns = [
    path('clients/create/', CreateUserAPIView.as_view(), name='create_user'),
]
