from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import GameItem
from .serializers import GameItemSerializer

class GameItemListView(generics.ListCreateAPIView):
    queryset = GameItem.objects.all()
    serializer_class = GameItemSerializer
    permission_classes = [IsAuthenticated]
