
class Node:
    def __init__(self, value, prev=None, next_=None, list_=None):
        self.value = value
        self._prev = prev
        self._next = next_
        self._list = list_

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @property
    def list(self):
        return self._list

    def _erase(self):
        self._next = None
        self._prev = None
        self._list = None


class LinkedList:

    END_NODE = Node(None)

    def __init__(self):
        self.END_NODE._list = self
        self._head = self.END_NODE
        self._tail = self.END_NODE
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self._head
        while current is not self._tail:
            yield current
            current = current.next

    def begin(self) -> Node:
        return self._head

    def end(self) -> Node:
        return self._tail

    def insert(self, value, before: Node = END_NODE):
        self._is_node_valid(before)
        self._insert(value, before.prev or None, before)

    def erase(self, node: Node):
        self._is_node_valid(node)
        if node is self.END_NODE:
            raise ValueError("Can't erase END_NODE")
        self._erase(node.prev, node, node.next)

    def _is_node_valid(self, node):
        if not isinstance(node, Node):
            raise ValueError("Node is not instance of 'Node'")
        if node is None:
            raise ValueError("Node is None")
        if node.list is not self:
            raise ValueError("Node doesn't belong to list")

    def _insert(self, value, after: Node, before: Node):
        node = Node(value, prev=after, next_=before, list_=self)

        if after is not None:
            after._next = node
        else:
            self._head = node

        before._prev = node
        self._size += 1

    def _erase(self, before: Node, node: Node, after: Node):
        if before is not None:
            before._next = after
        else:
            self._head = after

        after._prev = before
        node._erase()

        self._size -= 1
