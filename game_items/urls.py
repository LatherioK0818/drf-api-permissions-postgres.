from django.urls import path
from .views import GameItemListView, GameItemDetailView

urlpatterns = [
    path("api/game_items/", GameItemListView.as_view(), name="game-item-list"),
    path("api/game_items/<int:pk>/", GameItemDetailView.as_view(), name="game-item-detail"),
]