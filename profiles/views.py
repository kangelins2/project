from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Profile
from .serializers import UserSerializer, ProfileCreateSerializer, ProfileDeleteSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsAuthenticated]


class ProfileDeleteView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDeleteSerializer
    permission_classes = [IsAuthenticated]