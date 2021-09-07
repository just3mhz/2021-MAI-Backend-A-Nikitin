from llist import LinkedList, Node


class LRUCache:
    def __init__(self, capacity: int = 16):
        self._capacity = capacity
        self._items = LinkedList()
        self._nodes_hashmap: dict[str, Node] = {}

    def get(self, key: str) -> str:
        node = self._nodes_hashmap.get(key, None)
        if node is None:
            return ""
        return node.value[1]

    def set(self, key: str, value: str) -> None:
        node = self._nodes_hashmap.get(key, None)

        if node is not None:
            self._items.erase(node)
            self._items.insert((key, value), self._items.begin())
            return

        self._items.insert((key, value), self._items.begin())
        self._nodes_hashmap[key] = self._items.begin()

        while len(self._items) > self._capacity:
            last_used = self._items.end().prev
            del self._nodes_hashmap[last_used.value[0]]
            self._items.erase(last_used)

    def rem(self, key: str) -> None:
        node = self._nodes_hashmap.get(key, None)
        if node is not None:
            del self._nodes_hashmap[key]
            self._items.erase(node)

    def _reuse(self, node, new_value):
        self._items.erase(node)
        self._items.insert((node.value[0], new_value), self._items.begin())
        self._nodes_hashmap[node.value[0]] = self._items.begin()
