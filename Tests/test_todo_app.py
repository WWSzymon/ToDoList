# test_todo_app.py
import unittest
from todo_app import ToDoApp

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        """Inicjalizuje nową aplikację ToDoApp przed każdym testem."""
        self.app = ToDoApp()

    def test_add_task(self):
        """Test dodania zadania do listy."""
        self.assertTrue(self.app.add_task("Kupić mleko"))
        self.assertIn("Kupić mleko", self.app.list_tasks())

    def test_add_empty_task(self):
        """Test próby dodania pustego zadania."""
        self.assertFalse(self.app.add_task(""))
        self.assertFalse(self.app.add_task(None))
        self.assertEqual(self.app.list_tasks(), [])

    def test_remove_task(self):
        """Test usunięcia istniejącego zadania."""
        self.app.add_task("Kupić mleko")
        self.assertTrue(self.app.remove_task("Kupić mleko"))
        self.assertNotIn("Kupić mleko", self.app.list_tasks())

    def test_remove_nonexistent_task(self):
        """Test próby usunięcia zadania, które nie istnieje."""
        self.assertFalse(self.app.remove_task("Nieistniejące zadanie"))

    def test_list_tasks_initially_empty(self):
        """Test sprawdzający, czy lista zadań jest pusta na początku."""
        self.assertEqual(self.app.list_tasks(), [])

    def test_list_tasks_with_tasks(self):
        """Test dodania wielu zadań i ich wyświetlenia."""
        self.app.add_task("Kupić mleko")
        self.app.add_task("Zadzwonić do lekarza")
        self.assertEqual(self.app.list_tasks(), ["Kupić mleko", "Zadzwonić do lekarza"])

    def test_add_multiple_tasks(self):
        """Test dodania wielu zadań i sprawdzenia ich obecności na liście."""
        tasks = ["Kupić mleko", "Sprzątnąć pokój", "Zadzwonić do lekarza"]
        for task in tasks:
            self.app.add_task(task)
        self.assertEqual(self.app.list_tasks(), tasks)

    def test_remove_task_only_one_left(self):
        """Test usunięcia jedynego zadania na liście."""
        self.app.add_task("Zadanie")
        self.assertTrue(self.app.remove_task("Zadanie"))
        self.assertEqual(self.app.list_tasks(), [])

    def test_remove_all_tasks(self):
        """Test usunięcia wszystkich zadań po ich dodaniu."""
        tasks = ["Kupić mleko", "Sprzątnąć pokój"]
        for task in tasks:
            self.app.add_task(task)
        for task in tasks:
            self.app.remove_task(task)
        self.assertEqual(self.app.list_tasks(), [])

    def test_readd_removed_task(self):
        """Test dodania zadania, które zostało wcześniej usunięte."""
        self.app.add_task("Zadanie")
        self.app.remove_task("Zadanie")
        self.assertTrue(self.app.add_task("Zadanie"))
        self.assertIn("Zadanie", self.app.list_tasks())

    def test_remove_partially_filled_task(self):
        """Test dodania częściowego zadania (spacja) i usunięcia go."""
        self.app.add_task(" ")
        self.assertTrue(self.app.remove_task(" "))
        self.assertEqual(self.app.list_tasks(), [])

    def test_add_duplicate_task(self):
        """Test dodania duplikatu zadania."""
        self.app.add_task("Zadanie")
        self.assertTrue(self.app.add_task("Zadanie"))
        self.assertEqual(self.app.list_tasks().count("Zadanie"), 2)

    def test_remove_duplicate_task_once(self):
        """Test usunięcia jednego z duplikatów zadania."""
        self.app.add_task("Zadanie")
        self.app.add_task("Zadanie")
        self.app.remove_task("Zadanie")
        self.assertIn("Zadanie", self.app.list_tasks())
        self.assertEqual(self.app.list_tasks().count("Zadanie"), 1)

    def test_large_number_of_tasks(self):
        """Test dodania dużej liczby zadań i sprawdzenia, czy wszystkie się dodają."""
        tasks = [f"Zadanie {i}" for i in range(100)]
        for task in tasks:
            self.app.add_task(task)
        self.assertEqual(len(self.app.list_tasks()), 100)
        self.assertEqual(self.app.list_tasks(), tasks)

    def test_clear_all_tasks(self):
        """Test wyczyszczenia listy poprzez usunięcie wszystkich zadań."""
        tasks = ["Zadanie 1", "Zadanie 2", "Zadanie 3"]
        for task in tasks:
            self.app.add_task(task)
        for task in tasks:
            self.app.remove_task(task)
        self.assertEqual(self.app.list_tasks(), [])

if __name__ == "__main__":
    unittest.main()
