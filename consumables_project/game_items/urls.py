from django.urls import path
from .views import GameItemListView, GameItemDetailView

urlpatterns = [
    path("api/game-items/", GameItemListView.as_view(), name="game-item-list"),
    path("api/game-items/<int:pk>/", GameItemDetailView.as_view(), name="game-item-detail"),
]