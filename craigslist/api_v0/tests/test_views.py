from datetime import datetime
from unittest import mock

from django.test import TestCase

from rest_framework import status

from ..models import User
from ..models import Category
from ..models import Advertisement

from ..serializers import UserSerializer
from ..serializers import CategorySerializer
from ..serializers import AdvertisementSerializer


class TestUserView(TestCase):
    fixtures = ['user_fixture.json']

    def setUp(self) -> None:
        pass

    def test_get_all_users(self) -> None:
        response = self.client.get('/api/v0/users/')

        all_users = User.objects.all().order_by('-date_joined')
        expected = UserSerializer(all_users, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)

    def test_retrieve_one_user(self) -> None:
        response = self.client.get('/api/v0/users/1/')
        expected = UserSerializer(User.objects.get(pk=1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)

    def test_user_not_found(self) -> None:
        response = self.client.get('/api/v0/users/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestCategoryView(TestCase):
    fixtures = ['category_fixture.json',
                'user_fixture.json',
                'advertisement_fixture.json']

    def setUp(self) -> None:
        pass

    def test_get_all_categories(self) -> None:
        response = self.client.get('/api/v0/categories/')
        expected = CategorySerializer(Category.objects.all(), many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)

    def test_retrieve_category(self) -> None:
        response = self.client.get('/api/v0/categories/1/')
        expected = AdvertisementSerializer(
            Advertisement.objects.filter(category_id=1).order_by('-pub_date'),
            many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)


class TestAdvertisementView(TestCase):
    fixtures = ['category_fixture.json',
                'user_fixture.json',
                'advertisement_fixture.json']

    def setUp(self) -> None:
        pass

    def test_get_all_advertisements(self) -> None:
        response = self.client.get('/api/v0/advertisements/')
        expected = AdvertisementSerializer(
            Advertisement.objects.all().order_by('-pub_date'), many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)

    def test_retrieve_advertisement(self) -> None:
        response = self.client.get('/api/v0/advertisements/1/')
        expected = AdvertisementSerializer(
            Advertisement.objects.get(pk=1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected.data)

    def test_create_advertisement(self) -> None:
        request_data = {
            "title": "New advertisement",
            "description": "Useful description",
            "price": 0,
            "pub_date": datetime.now().date(),
            "published": True,
            "user": 0,
            "category": 0
        }

        response = self.client.post('/api/v0/advertisements/', request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        advertisement = Advertisement.objects.get(pk=response.data["advertisement_id"])
        self.assertEqual(request_data["title"], advertisement.title)
        self.assertEqual(request_data["pub_date"], advertisement.pub_date)

    @mock.patch("api_v0.forms.AdvertisementForm.is_valid", return_value=False)
    def test_create_advertisement_wrong_data(self, mocked) -> None:
        request_data = {
            "title": "New advertisement",
            "description": "Useful description",
            "price": 0,
            "pub_date": datetime.now().date(),
            "published": True,
            "user": 0,
            "category": 0
        }

        response = self.client.post('/api/v0/advertisements/', request_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"errors": {}})

    def test_delete_advertisement(self) -> None:
        response = self.client.delete('/api/v0/advertisements/0/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Advertisement.DoesNotExist, Advertisement.objects.get, pk=0)
