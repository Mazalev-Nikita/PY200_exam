from typing import Any, Optional

class Node:

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self.prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self.__prev = prev

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"
        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

if __name__ == "__main__":
    node1 = Node(1)
    node2 = DoubleLinkedNode(2)
    print(node1, node2)
