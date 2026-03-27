class Node:
    def __init__(self, size, next):
        self._array = [None for i in range(size)]  # stała tablica
        self._count = 0
        self._next = next


class unrolledLinkedList:
    def __init__(self, node_max_size=4):
        self._head = None
        self._node_max_size = node_max_size

    def get(self, idx):
        curr_node = self._head
        while curr_node is not None:
            if idx < curr_node._count:
                return curr_node._array[idx]
            idx -= curr_node._count
            curr_node = curr_node._next
        return None  # jeśli indeks wyjdzie poza zakres całej listy

    def insert(self, data, idx):
        if self._head == None:
            self._head = Node(self._node_max_size, None)
            self._head._array[0] = data
            self._head._count = 1
        curr_node = self._head
        while curr_node is not None:
            if idx <= curr_node._count or curr_node._next is None:
                # pełen element i dzielenie na pół
                if curr_node._count == self._node_max_size:
                    half = self._node_max_size // 2
                    new_node = Node(self._node_max_size, curr_node._next)

                    for i in range(half, self._node_max_size):
                        new_node._array[i - half] = curr_node._array[i]
                        curr_node._array[i] = None

                    new_node._count = self._node_max_size - half
                    curr_node._count = half
                    curr_node._next = new_node

                    if idx > curr_node._count:
                        idx -= curr_node._count
                        curr_node = new_node

                # element, w którym jest miejsce

                for i in range(curr_node._count, idx, step=-1):
                    curr_node._array[i] = curr_node._array[i - 1]
                curr_node._array[idx] = data
                curr_node._count += 1
                return
            idx -= curr_node._count
            curr_node = curr_node._next
