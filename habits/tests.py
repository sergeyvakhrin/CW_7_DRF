from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.data = {
            'habit': "Test",
            'sing_habit': False,
            'reward': 1,
            'sing_publicity': True
        }
        self.user = User.objects.create(email='admin@sky.pro')
        self.habit = Habit.objects.create(**self.data, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        response = self.client.post('/habits/create/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        response = self.client.get('/habits/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_list_public(self):
        response = self.client.get('/habits/list-publiс/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve(self):
        url = reverse('habits:habit-get', args=(self.habit.pk, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse('habits:habit-update', args=(self.habit.pk, ))
        data = {
            'sing_publicity': False
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        url = reverse('habits:habit-delete', args=(self.habit.pk, ))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
