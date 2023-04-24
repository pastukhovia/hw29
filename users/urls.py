from django.urls import path
from .views import UserDetailAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView, UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
    path('<int:pk>/update/', UserUpdateAPIView.as_view()),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view()),
]
