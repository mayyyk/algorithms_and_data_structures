import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Inicjalizacja nowej listy przed każdym testem."""
        self.list = LinkedList()

    def test_initialization(self):
        self.assertTrue(self.list.is_empty())
        self.assertEqual(self.list.length(), 0)

    def test_add_elements(self):
        self.list.add("A")
        self.list.add("B")
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(), "B")  # B powinno być nową głową

    def test_append_elements(self):
        self.list.append("A")
        self.list.append("B")
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(), "A")  # A powinno pozostać głową

    def test_remove_head(self):
        self.list.append("A")
        self.list.append("B")
        removed = self.list.remove()
        self.assertEqual(removed, "A")
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(), "B")

    def test_remove_end(self):
        self.list.append("A")
        self.list.append("B")
        removed = self.list.remove_end()
        self.assertEqual(removed, "B")
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(), "A")

    def test_single_element_logic(self):
        """Kluczowy test: czy po usunięciu jedynego elementu head i tail są None."""
        self.list.add("OnlyOne")
        self.list.remove()
        self.assertTrue(self.list.is_empty())
        self.assertIsNone(self.list._head)
        self.assertIsNone(self.list._tail)

    def test_destroy(self):
        for i in range(10):
            self.list.append(i)
        self.list.destroy()
        self.assertTrue(self.list.is_empty())
        self.assertEqual(self.list.length(), 0)

    def test_reverse_consistency(self):
        """Sprawdza czy wskaźniki _prev są poprawne."""
        data = ["A", "B", "C"]
        for d in data:
            self.list.append(d)
        # Porównujemy reprezentację tekstową w obie strony
        fwd = str(self.list)
        rev = self.list.reverse_print()
        self.assertIn("A", fwd)
        self.assertIn("C", rev)


if __name__ == "__main__":
    unittest.main()
