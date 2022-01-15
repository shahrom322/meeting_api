from django.urls import path

from core.views import CreateUserAPIView, UserMatchAPIView, UserListAPIView

urlpatterns = [
    path('clients/create/', CreateUserAPIView.as_view(), name='create_user'),
    path('clients/<int:pk>/match/', UserMatchAPIView.as_view(), name='match'),
    path('list/', UserListAPIView.as_view(), name='list'),
]
