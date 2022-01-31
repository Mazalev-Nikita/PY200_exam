from typing import Sequence, Any, Iterable, Optional

from Node import Node, DoubleLinkedNode

from _collections_abc import MutableSequence


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    @property
    def _len(self):
        return self.__len

    @_len.setter
    def _len(self, len_value):
        if not isinstance(len_value, int):
            raise TypeError()
        elif len_value < 0:
            raise ValueError()
        self.__len = len_value


    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self._len += 1
    def __len__(self):
        return self._len

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1


    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"
    def __str__(self) -> str:
        return f"{self.to_list()}"
    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1


class DoubleLinkedList(LinkedList):

    def __init__(self, data: Sequence = None):
        """Конструктор двусвязного списка"""
        super().__init__(data)

    def __linked_nodes(self, left: DoubleLinkedNode, right: Optional[DoubleLinkedNode]) -> None:
        if not right:
            self.tail = left
        elif not left:
            self.head = right
        else:
            left.next = right
            right.prev = left


    def append(self, value: Any):
        append_node = self.DoubleLinkedNode(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            self.__linked_nodes(self.tail, append_node)
            self.tail = append_node
        self._len += 1
    def insert(self, index: int, value: Any):
        insert_node = self.DoubleLinkedNode(value)
        if index == 0:
            self.__linked_nodes(insert_node, self.head)
            self.head = insert_node
            self._len += 1
        elif 0 < index < self._len:
            next_node = self.step_by_step_on_nodes(index)
            prev_node = next_node.prev
            self.__linked_nodes(prev_node, insert_node)
            self.__linked_nodes(insert_node, next_node)
            self._len += 1
        elif index >= self._len:
            self.append(value)

    def remove(self, value: Any) -> None:
        search_result = False
        for current_value in self.__iter__():
            if value == current_value.value:
                prev_node = current_value.prev
                next_node = current_value.next
                self.__linked_nodes(prev_node, next_node)
                self._len -= 1
                search_result = True
                break
        if not search_result:
            raise ValueError(f'{value} not in list')


if __name__ == '__main__':
    ll = LinkedList('abcdefg')
    # l = iter(ll)
    ll.insert(2, 'B')
    ll.remove('e')
    print(ll)
