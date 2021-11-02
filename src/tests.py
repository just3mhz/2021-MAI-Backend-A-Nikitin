import unittest

from collections import OrderedDict

from cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self) -> None:
        self.lru = LRUCache(capacity=4)
        self.lru._cache = OrderedDict([("1", "1"), ("2", "2"), ("3", "3")])

    def test_get(self):
        self.assertEqual(self.lru.get("1"), "1")
        self.assertEqual(self.lru.get("2"), "2")
        self.assertEqual(self.lru.get("3"), "3")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("1", "1"), ("2", "2"), ("3", "3")])

    def test_get_non_existing(self):
        self.assertEqual(self.lru.get("key"), "")

    def test_set(self):
        self.lru.set("4", "4")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")])

        self.lru.set("4", "4.1")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4.1")])

        self.lru.set("5", "5")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("2", "2"), ("3", "3"), ("4", "4.1"), ("5", "5")])

    def test_rem(self):
        self.lru.rem("1")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("2", "2"), ("3", "3")])

        self.lru.rem("2")
        self.assertListEqual(
            list(self.lru._cache.items()),
            [("3", "3")])
