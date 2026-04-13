class QueueElement:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority

    def __lt__(self, other):
        if self._priority < other._priority:
            return True

    def __gt__(self, other):
        if self._priority > other._priority:
            return True

    def __repr__(self):
        return self._priority, self._data


class PriorityQueue:
    def __int__(self):
        self.tab = None
        self.heap_size = None

    def is_empty(self):
        if len(self._array) == 0:
            return True

    def peek(self):
        pass

    def dequeue(self):
        return_element = self._tab[0]
        self._repair()
        self._size -= 1

        return return_element

    def _repair(self):
        pass

    def enqueue(self, element):
        pass

    def left(self, idx):
        pass

    def left(self, idx):
        pass

    def parent(self, idx):
        pass

    def print_tab(self):
        print("{", end=" ")
        print(*self.tab[: self.heap_size], sep=", ", end=" ")
        print("}")

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * "  ", self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def main():
    pQueue = PriorityQueue()
    pQueue.print_tree(0, 0)

    for priority, data in zip([7, 5, 1, 2, 5, 3, 4, 8, 9], "GRYMOTYLA"):
        pQueue.enqueue(QueueElement(data, priority))

    pQueue.print_tree(0, 0)
    pQueue.print_tab()

    deq_el = pQueue.dequeue()

    print(pQueue.peek())
    pQueue.print_tab()

    print(deq_el)

    for _ in range(pQueue.heap_size):
        deq_el = pQueue.dequeue()
        print(deq_el)

    pQueue.print_tab()


main()
