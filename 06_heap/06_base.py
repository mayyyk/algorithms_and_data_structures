class QueueElement:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f"{self.__priority} : {self.__data}"


class PriorityQueue:
    def __init__(self):
        self.__tab = []
        self.__heap_size = 0

    def is_empty(self):
        return self.__heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.__tab[0]

    def dequeue(self):
        return_element = self.__tab[0]
        self.__tab[0] = self.__tab[
            self.__heap_size - 1
        ]  # zamiana w ten sposób, bo wtedy gwarancja, że stos nie ma dziur i naprawa będzie prosta, bo tylko jeden element nie pasuje
        self.__heap_size -= 1
        self._repair_down(0)  # start od nowego elementu na pierwszm miejscu
        return return_element

    def _repair_down(
        self, idx
    ):  # dla naprawiania w dół, czyli w przypadku usuwania pierwszego elementu stosu.
        l = self._left(idx)
        r = self._right(idx)
        largest = idx

        # sprawdzenie, który jest najważniejszy
        if l < self.__heap_size and self.__tab[l] > self.__tab[largest]:
            largest = l
        if r < self.__heap_size and self.__tab[r] > self.__tab[largest]:
            largest = r

        if largest != idx:
            self.__tab[largest], self.__tab[idx] = self.__tab[idx], self.__tab[largest]
            self._repair_down(largest)

    def _repair_up(
        self, idx
    ):  # dla naprawiania w górę, czyli w przypadku dodawania nowego elementu na koniec listy w enqueue
        if idx == 0:
            return
        parent_idx = self._parent(idx)
        if self.__tab[parent_idx] < self.__tab[idx]:
            self.__tab[parent_idx], self.__tab[idx] = (
                self.__tab[idx],
                self.__tab[parent_idx],
            )
            self._repair_up(parent_idx)

    def enqueue(self, element):
        if self.__heap_size == len(self.__tab):
            self.__tab.append(element)
        else:
            self.__tab[self.__heap_size] = element
        self.__heap_size += 1
        self._repair_up(self.__heap_size - 1)

    def _left(self, idx):
        return 2 * idx + 1

    def _right(self, idx):
        return 2 * idx + 2

    def _parent(self, idx):
        return (idx - 1) // 2

    def print_tab(self):
        print("{", end=" ")
        print(*self.__tab[: self.__heap_size], sep=", ", end=" ")
        print("}")

    def print_tree(self, idx, lvl):
        if idx < self.__heap_size:
            self.print_tree(self._right(idx), lvl + 1)
            print(2 * lvl * "  ", self.__tab[idx] if self.__tab[idx] else None)
            self.print_tree(self._left(idx), lvl + 1)

    def get_heap_size(self):
        return self.__heap_size


def main():

    pQueue = PriorityQueue()

    for priority, data in zip([7, 5, 1, 2, 5, 3, 4, 8, 9], "GRYMOTYLA"):
        pQueue.enqueue(QueueElement(data, priority))

    pQueue.print_tree(0, 0)
    pQueue.print_tab()

    deq_el = pQueue.dequeue()

    print(pQueue.peek())
    pQueue.print_tab()

    print(deq_el)

    for _ in range(pQueue.get_heap_size()):
        deq_el = pQueue.dequeue()
        print(deq_el)

    pQueue.print_tab()


main()
