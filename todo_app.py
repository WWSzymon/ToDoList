class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Dodaj zadanie do listy."""
        if task:
            self.tasks.append(task)
            return True
        return False

    def remove_task(self, task):
        """Usuń zadanie z listy."""
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self):
        """Zwraca listę zadań."""
        return self.tasks


def main():
    app = ToDoApp()

    while True:
        print("\nWybierz akcję:")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Wyświetl listę zadań")
        print("4. Wyjście")

        choice = input("Wpisz numer akcji: ")

        if choice == '1':
            task = input("Wpisz zadanie do dodania: ")
            if app.add_task(task):
                print(f"Zadanie '{task}' zostało dodane.")
            else:
                print("Nie udało się dodać zadania (puste zadanie).")

        elif choice == '2':
            task = input("Wpisz zadanie do usunięcia: ")
            if app.remove_task(task):
                print(f"Zadanie '{task}' zostało usunięte.")
            else:
                print("Nie znaleziono zadania na liście.")

        elif choice == '3':
            tasks = app.list_tasks()
            if tasks:
                print("\nLista zadań:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("Lista zadań jest pusta.")

        elif choice == '4':
            print("Zakończenie programu.")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()
