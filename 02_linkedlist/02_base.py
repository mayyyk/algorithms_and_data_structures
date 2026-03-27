class LinkedList:
    def __init__(self):
        self._head = None  # wskazanie na pierwszy element listy

    def destroy(self):
        self._head = None  # usunięcie referencji do dalszych elementów listy automatycznie usuwa całą listę

    def add(self, data):
        # dodawany wskazuje na head
        if self.is_empty():
            self._head = LinkedListElement(data, None)
        else:  # gdy head już istnieje, add to wpinanie się między head a poprzedni pierwszy element
            new_element = LinkedListElement(data, self._head)
            self._head = new_element

    def append(self, data):
        if self.is_empty():
            self._head = LinkedListElement(data, None)
        else:
            current_element = self._head
            while current_element._next != None:
                current_element = current_element._next
            current_element._next = LinkedListElement(data, None)

    def remove(self):
        if self.is_empty():
            return
        self._head = self._head._next

    def remove_end(self):
        if self.is_empty():
            return

        if self.length() == 1:
            self._head = None
            return

        current_element = self._head
        prev_element = None
        while current_element._next != None:
            prev_element = current_element
            current_element = current_element._next
        prev_element._next = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def length(self):
        if self.is_empty():
            return 0
        current_element = self._head
        list_len = 0  # nie zaczyna się od 1 bo while kończy się, gdy obecny element jest None, czyli dodatkowa iteracja
        while current_element != None:
            list_len += 1
            current_element = current_element._next
        return list_len

    def get(self):
        if not self.is_empty():
            return self._head._data
        else:
            return None

    def __str__(self):
        if self.is_empty():
            return ""
        current_element = self._head
        print_str = ""
        while current_element != None:
            data = current_element._data
            data_str = f"\n -> {data}"
            print_str += data_str
            current_element = current_element._next
        return print_str + "\n"


class LinkedListElement:
    def __init__(self, data, next):
        self._data = (
            data  # referencja (wskazanie) do danych w danej instancji elementu listy
        )
        self._next = next  # referencja (wskazanie) do kolejnego obiektu


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

    print("Powinny być 3 uczelnie")
    print(uczelnie)

    for school in schools[3:]:
        uczelnie.add(school)

    print("Powinny być wszystkie uczelnie")
    print(uczelnie)

    print("Powinno być 6")
    print(uczelnie.length())

    uczelnie.remove()
    print("Powinen być UP")
    print(uczelnie.get())

    uczelnie.remove_end()
    print("Powinno nie być PG na końcu")
    print(uczelnie)

    uczelnie.destroy()
    print("Powinno być True")
    print(uczelnie.is_empty())

    uczelnie.remove()
    uczelnie.remove_end()

    print("Powinno być puste")
    print(uczelnie)
    print("----")

    uczelnie.append(schools[0])
    print(uczelnie.get())

    uczelnie.remove_end()  # sprawdzić, czy dobrze usuwa ostatni element
    print("Powinno być True")
    print(uczelnie.is_empty())
    print(uczelnie)


main()
