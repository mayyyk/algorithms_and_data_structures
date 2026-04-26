import random, time


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
    def __init__(self, tab=None):
        self.__tab = tab
        self.__heap_size = 0
        if tab is not None:
            self.__heap_size = len(self.__tab)
            self._build_heap()

    def is_empty(self):
        return self.__heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.__tab[0]

    def dequeue(self):
        return_element = self.__tab[0]
        self.__tab[0], self.__tab[self.__heap_size - 1] = (
            self.__tab[self.__heap_size - 1],
            self.__tab[0],
        )
        self.__heap_size -= 1
        self._repair_down(0)
        return return_element

    def _build_heap(self):
        start_idx = (self.__heap_size - 2) // 2
        for idx in range(start_idx, -1, -1):
            self._repair_down(idx)

    def sort(self):
        while self.__heap_size > 1:
            self.dequeue()

    def _repair_down(self, idx):
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


def swap(tab):
    for i in range(0, len(tab)):
        min_idx = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]


def shift(tab):
    for i in range(0, len(tab)):
        min_idx = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        min_el = tab.pop(min_idx)
        tab.insert(i, min_el)


def test1():
    input_data = [
        (5, "A"),
        (5, "B"),
        (7, "C"),
        (2, "D"),
        (5, "E"),
        (1, "F"),
        (7, "G"),
        (5, "H"),
        (1, "I"),
        (2, "J"),
    ]

    tab_heap = [QueueElement(value, priority) for priority, value in input_data]

    pq = PriorityQueue(tab_heap)

    pq.print_tab()
    pq.print_tree(0, 0)

    pq.sort()

    print(tab_heap)

    print("NIESTABILNE")

    tab_swap = [QueueElement(v, p) for p, v in input_data]
    swap(tab_swap)
    print(tab_swap)
    print("NIESTABILNE")

    tab_shift = [QueueElement(v, p) for p, v in input_data]
    shift(tab_shift)
    print(tab_shift)
    print("STABILNE")


def test2():
    original_data = [int(random.random() * 100) for _ in range(10000)]

    data_for_heap = list(original_data)
    t_start = time.perf_counter()
    pq = PriorityQueue(data_for_heap)
    pq.sort()
    t_stop = time.perf_counter()
    print("Heapsort - czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    data_for_swap = list(original_data)
    t_start = time.perf_counter()
    swap(data_for_swap)
    t_stop = time.perf_counter()
    print("Selection Sort (Swap) - czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # 3. Test Selection Sort Shift
    data_for_shift = list(original_data)
    t_start = time.perf_counter()
    shift(data_for_shift)
    t_stop = time.perf_counter()
    print("Selection Sort (Shift) - czas obliczeń:", "{:.7f}".format(t_stop - t_start))


def main():
    test_type = input()
    if test_type == "1":
        test1()
    elif test_type == "2":
        test2()
    else:
        return


main()
