from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class PrisingTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testov@test.ru',
            username='test',
            password="12345",
            login_as=True
        )
        self.client.force_authenticate(user=self.user)

    def test_create_prising(self):
        # self.client.force_authenticate(user=self.user)
        url = reverse("pricing:price-create")
        data = {
            "original_price": "100.00",
        }
        response = self.client.post(url, data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
