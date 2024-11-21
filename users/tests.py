from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        pass
        self.user = User.objects.create(email="admin@sky.pro")
        # self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        # url = reverse('users:users')
        data = {
            "email": "parlamentsv@mail.ru",
            "password": "1234",
            "is_active": "True",
            "is_staff": "True",
            "is_superuser": "True",
        }
        response = self.client.post("/users/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
