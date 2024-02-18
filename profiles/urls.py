from django.urls import include
from django.urls import path
from profiles.views import UserCreateView, ProfileCreateView, ProfileDeleteView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
