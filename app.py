"""A tiny command-line task manager."""

tasks = []


def add_task(title):
    """Add a task and return the created task."""
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")

    task = {"title": title.strip(), "completed": False}
    tasks.append(task)
    return task


def list_tasks():
    """Return all tasks."""
    return tasks


def complete_task(index):
    """Mark a task as completed using its zero-based index."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Task not found.")

    tasks[index]["completed"] = True
    return tasks[index]


def main():
    print("Simple Task Manager")
    while True:
        print("\n1. Add task  2. List tasks  3. Complete task  4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                add_task(title)
                print("Task added.")
            except ValueError as error:
                print(error)
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            for number, task in enumerate(list_tasks(), start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{number}. [{status}] {task['title']}")
        elif choice == "3":
            try:
                number = int(input("Task number to complete: "))
                complete_task(number - 1)
                print("Task marked as completed.")
            except (ValueError, IndexError):
                print("Please enter a valid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
