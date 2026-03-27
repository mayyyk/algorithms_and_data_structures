class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self._array = [None for i in range(size)]
        self._size = size
        self._c1 = c1
        self._c2 = c2
        self._deleted = DeletedElement()

    def search(self, key):
        base_index = self._hash(key)
        iteration = 0
        while iteration <= self._size - 1:
            current_index = self._probing(base_index, iteration)
            if (
                isinstance(self._array[current_index], Element)
                and self._array[current_index]._key == key
            ):
                return self._array[current_index]._value
            elif self._array[current_index] == None:
                return None  # jeśli tu jest None, to dalej też nic nie będzie
            elif (
                isinstance(self._array[current_index], Element)
                and self._array[current_index]._key != key
            ) or (self._array[current_index] is self._deleted):
                pass  # po prostu przejście do kolejnej iteracji dla danego klucza
            iteration += 1
        return None

    def insert(self, key, data):
        base_index = self._hash(key)
        iteration = 0
        while iteration <= self._size - 1:
            current_index = self._probing(base_index, iteration)
            if self._array[current_index] == None or (
                self._array[current_index] is self._deleted
            ):
                self._array[current_index] = Element(key, data)
                return
            elif (
                isinstance(self._array[current_index], Element)
                and self._array[current_index]._key == key
            ):
                self._array[current_index]._value = data
                return
            elif (
                isinstance(self._array[current_index], Element)
                and self._array[current_index]._key != key
            ):
                pass  # przejście do kolejnej iteracji i wyznaczenia nowego indeksu dla klucza
            iteration += 1
        raise Exception("Brak miejsca")

    def remove(self, key):
        base_index = self._hash(key)
        iteration = 0
        while iteration <= self._size - 1:
            current_index = self._probing(base_index, iteration)
            if (
                isinstance(self._array[current_index], Element)
                and self._array[current_index]._key == key
            ):
                self._array[current_index] = self._deleted
                return
            elif self._array[current_index] == None:
                break
            elif self._array[current_index] is self._deleted:
                pass
            iteration += 1
        raise Exception("Brak danej o podanym kluczu")

    def __str__(self):
        element_strings = [str(el) if el is not None else "None" for el in self._array]
        return "{" + ", ".join(element_strings) + "}"

    # HELPERS

    def _hash(self, key):
        if isinstance(key, str):
            value = sum(ord(char) for char in key)
        else:
            value = int(key)
        base_index = value % self._size
        return base_index

    def _probing(self, base_index, iteration):
        new_index = base_index + iteration * self._c1 + (iteration**2) * self._c2
        return new_index % self._size

    # def _find_slot(self, key):


class Element:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def __str__(self):
        return f"{self._key}:{self._value}"


class DeletedElement:
    def __str__(self):
        return "None"


def test_func_1(size, c1=1, c2=0):
    table_1 = HashTable(size, c1, c2)
    values = [chr(65 + i) for i in range(15)]

    for i in range(15):
        key = i + 1
        if key == 6:
            key = 18
        elif key == 7:
            key = 31

        value = values[i]

        try:
            table_1.insert(key, value)
        except Exception as e:
            print(e)

    print(table_1)

    print(table_1.search(5))

    print(table_1.search(14))
    table_1.insert(5, "Z")

    print(table_1.search(5))

    table_1.remove(5)
    print(table_1)

    print(table_1.search(31))

    table_1.insert("test", "W")
    print(table_1)


def test_func_2(size, c1=1, c2=0):
    table_1 = HashTable(size, c1, c2)
    values = [chr(65 + i) for i in range(15)]
    keys = [13 * (i + 1) for i in range(15)]

    for idx in range(15):
        try:
            table_1.insert(keys[idx], values[idx])
        except Exception as e:
            print(e)

    print(table_1)


def main():
    test_func_1(13)
    test_func_2(13)  # wszystkie miejsca zajęte
    test_func_2(
        13, 0, 1
    )  # dużo niezajętych, bo próbkowanie kwadratowe nie gwarantuje we wszytkie (nawet wolne) miejsca w tablicy
    test_func_1(13, 0, 1)  # tylko jedno nie zajęte


main()
