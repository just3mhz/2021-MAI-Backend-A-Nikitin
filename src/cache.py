from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int = 16):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: str) -> str:
        if value := self._cache.get(key, None):
            self._cache.move_to_end(key)
            return value
        return ""

    def set(self, key: str, value: str) -> None:
        if key in self._cache:
            del self._cache[key]
        self._cache[key] = value
        self._clean_up()

    def rem(self, key: str) -> None:
        if key in self._cache:
            del self._cache[key]

    def _clean_up(self):
        while len(self._cache) > self._capacity:
            self._cache.popitem(last=False)
