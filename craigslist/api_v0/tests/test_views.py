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
