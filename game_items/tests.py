# tests.py

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import GameItem

class GameItemTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='testuser',
            password='password'
        )
        test_user.save()

        test_game_item = GameItem.objects.create(
            owner=test_user,
            name='rake',
            description='Better for collecting leaves than a shovel.'
        )
        test_game_item.save()

    def test_game_item_model(self):
        game_item = GameItem.objects.get(id=1)
        self.assertEqual(game_item.owner.username, 'testuser')
        self.assertEqual(game_item.name, 'rake')
        self.assertEqual(game_item.description, 'Better for collecting leaves than a shovel.')

    def test_get_game_item_list(self):
        url = reverse('game-item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'rake')

    def test_get_game_item_by_id(self):
        url = reverse('game-item-detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'rake')

    def test_create_game_item(self):
        url = reverse('game-item-list')
        data = {'owner': 1, 'name': 'spoon', 'description': 'Good for cereal and soup.'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameItem.objects.count(), 2)
        self.assertEqual(GameItem.objects.get(id=2).name, 'spoon')

    def test_update_game_item(self):
        url = reverse('game-item-detail', args=(1,))
        data = {'owner': 1, 'name': 'rake', 'description': 'Pole with a crossbar toothed like a comb.'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        game_item = GameItem.objects.get(id=1)
        self.assertEqual(game_item.name, data['name'])
        self.assertEqual(game_item.owner.id, data['owner'])
        self.assertEqual(game_item.description, data['description'])

    def test_delete_game_item(self):
        url = reverse('game-item-detail', args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GameItem.objects.count(), 0)

