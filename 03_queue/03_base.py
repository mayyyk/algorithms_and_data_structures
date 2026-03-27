class cyclicArrayQueue:
    def __init__(self, size):
        self._array = [None for i in range(size)]
        self._size = size
        self._write_idx = 0
        self._read_idx = 0

    def is_empty(self):
        return self._read_idx == self._write_idx

    def peek(self):
        if self.is_empty():
            return None
        return self._array[self._read_idx]

    def enqueue(self, data):
        self._array[self._write_idx] = data

        if self._write_idx >= self._size - 1:
            self._write_idx = 0
        else:
            self._write_idx += 1

        if self._write_idx == self._read_idx:
            self.resize()

    def resize(self):
        new_size = self._size * 2
        new_write_idx = 0
        new_read_idx = 0
        new_array = [None for i in range(new_size)]
        new_order = self.get_logic_order()
        for element in new_order:
            new_array[new_write_idx] = element
            new_write_idx += 1
        self._size = new_size
        self._read_idx = new_read_idx
        self._write_idx = new_write_idx
        self._array = new_array

    def get_logic_order(self):
        data = []
        read_idx = self._read_idx
        steps = self._size
        for i in range(steps):
            element = self._array[read_idx]
            if element == None:
                return data
            data.append(element)
            if read_idx >= steps - 1:
                read_idx = 0
            else:
                read_idx += 1
        return data

    def dequeue(self):
        return_data = self._array[self._read_idx]
        self._array[self._read_idx] = None
        if self._read_idx >= self._size - 1:
            self._read_idx = 0
        else:
            self._read_idx += 1
        return return_data

    def state(self):
        return self._array

    def __str__(self):
        return f"{[element for element in self.get_logic_order()]}"


def main():
    queue_1 = cyclicArrayQueue(5)

    queue_1.enqueue(0)
    queue_1.enqueue(1)

    first_read = queue_1.dequeue()
    print(first_read)

    peek_read = queue_1.peek()
    print(peek_read)

    print(queue_1)

    for i in range(5, 9):
        queue_1.enqueue(i)

    array_state = queue_1.state()
    print(array_state)

    while not queue_1.is_empty():
        deleted_data = queue_1.dequeue()
        print(deleted_data)

    print(queue_1)


main()
