# urls.py

from django.urls import path
from .views import GameItemListView

urlpatterns = [
    path('api/v1/game-items/', GameItemListView.as_view(), name='game-item-list'),
    # Add other URL patterns as needed
]
