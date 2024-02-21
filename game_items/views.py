from rest_framework import generics
from .models import GameItem
from .serializers import GameItemSerializer

class GameItemListView(generics.ListCreateAPIView):
    queryset = GameItem.objects.all()
    serializer_class = GameItemSerializer
    
class GameItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameItem.objects.all()
    serializer_class = GameItemSerializer