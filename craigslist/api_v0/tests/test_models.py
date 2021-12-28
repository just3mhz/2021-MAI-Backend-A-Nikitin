from django.test import TestCase

from ..models import Category
from ..models import Advertisement


class TestCategoryModel(TestCase):
    fixtures = ['category_fixture.json']

    def test_str(self) -> None:
        category = Category.objects.get(pk=0)
        self.assertEqual(category.category, str(category))


class TestAdvertisementModel(TestCase):
    fixtures = ['advertisement_fixture.json',
                'category_fixture.json',
                'user_fixture.json']

    def test_str(self) -> None:
        advertisement = Advertisement.objects.get(pk=0)
        self.assertEqual(advertisement.title, str(advertisement))
