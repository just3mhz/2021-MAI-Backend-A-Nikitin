from collections import namedtuple

from typing import Dict

from llist import LinkedList, Node


class LRUCache:
    Item = namedtuple("Item", "key value")

    def __init__(self, capacity: int = 16):
        self._capacity = capacity
        self._items = LinkedList()
        self._nodes_hashmap: Dict[str, Node] = {}

    def get(self, key: str) -> str:
        if node := self._nodes_hashmap.get(key, None):
            self._remove(node)
            self._insert(node.value.key, node.value.value)
            return node.value.key
        # TODO: Is it necessary to add (key, "") to cache ?
        return ""

    def set(self, key: str, value: str) -> None:
        if node := self._nodes_hashmap.get(key, None):
            self._remove(node)
        self._insert(key, value)
        self._clean()

    def rem(self, key: str) -> None:
        if node := self._nodes_hashmap.get(key, None):
            self._remove(node)

    def _insert(self, key: str, value: str):
        self._items.insert(self.Item(key, value))
        self._nodes_hashmap[key] = self._items.begin()

    def _clean(self):
        while len(self._items) > self._capacity:
            last_used = self._items.end().prev
            self._remove(last_used)

    def _remove(self, node: Node):
        self._items.erase(node)
        del self._nodes_hashmap[node.value.key]
