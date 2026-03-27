class LinkedList:
    def __init__(self):
        self._head = None  # wskazanie na pierwszy element listy
        self._tail = None
        self._size = 0

    def destroy(self):
        if self.is_empty():
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return

        while not self.is_empty():
            self.remove()

    def add(self, data):
        # dodawany wskazuje na head
        if self.is_empty():
            self._head = LinkedListElement(data, None, None)
            self._tail = self._head
        else:  # gdy head już istnieje, add to wpinanie się między head a poprzedni pierwszy element
            old_head = self._head
            new_head = LinkedListElement(data, old_head, None)
            self._head = new_head
            old_head._prev = self._head
            # tail zostaje taki jak był
        self._size += 1

    def append(self, data):
        if self.is_empty():
            self._head = LinkedListElement(data, None, None)
            self._tail = self._head
        else:
            last_element = self._tail
            last_element._next = LinkedListElement(data, None, last_element)
            self._tail = last_element._next
        self._size += 1

    def remove(self):
        if self.is_empty():
            return
        if self._head == self._tail:
            self._tail = None
            self._head = None
            self._size = 0
            return
        new_head = self._head._next
        self._head = new_head
        self._head._prev = None
        self._size -= 1

    def remove_end(self):
        if self.is_empty():
            return

        if self._head == self._tail:
            self._head = None
            self._tail = None
            self._size = 0
            return

        last_element = self._tail
        new_last_element = last_element._prev
        self._tail = new_last_element
        self._tail._next = None
        self._size -= 1

    def is_empty(self):
        if self.length() == 0:
            return True
        return False

    def length(self):
        return self._size

    def get(self):
        if not self.is_empty():
            return self._head._data
        else:
            return None

    def __str__(self):
        if self.is_empty():
            return ""
        current_element = self._head
        elements = []
        while current_element != None:
            data = current_element._data
            elements.append(data)
            current_element = current_element._next
        return "\n -> ".join(map(str, elements))

    def reverse_print(self):
        if self.is_empty():
            return ""
        current_element = self._tail
        elements = []
        while current_element != None:
            data = current_element._data
            elements.append(data)
            current_element = current_element._prev
        return "\n <- ".join(map(str, elements))


class LinkedListElement:
    def __init__(self, data, next, prev):
        self._data = (
            data  # referencja (wskazanie) do danych w danej instancji elementu listy
        )
        self._next = next  # referencja (wskazanie) do kolejnego obiektu
        self._prev = prev


def main():
    schools = [
        ("AGH", "Kraków", 1919),
        ("UJ", "Kraków", 1364),
        ("PW", "Warszawa", 1915),
        ("UW", "Warszawa", 1915),
        ("UP", "Poznań", 1919),
        ("PG", "Gdańsk", 1945),
    ]

    uczelnie = LinkedList()
    uczelnie.append((schools[0]))
    uczelnie.append((schools[1]))
    uczelnie.append((schools[2]))

    print(uczelnie)
    print(uczelnie.reverse_print())

    for school in schools[3:]:
        uczelnie.add(school)

    print(uczelnie)
    print(uczelnie.reverse_print())

    print(uczelnie.length())

    uczelnie.remove()
    print(uczelnie.get())

    uczelnie.remove_end()
    print(uczelnie)
    print(uczelnie.reverse_print())

    uczelnie.destroy()
    print(uczelnie.is_empty())

    uczelnie.remove()
    uczelnie.remove_end()

    uczelnie.append(schools[0])
    print(uczelnie.get())

    uczelnie.remove_end()  # sprawdzić, czy dobrze usuwa ostatni element
    print(uczelnie.is_empty())
    print(uczelnie)
    print(uczelnie.reverse_print())


main()
