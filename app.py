
"""A simple command-line task manager."""

from datetime import datetime

tasks = []


def get_current_time():
    """Return the current local date and time."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def add_task(title):
    """Add a task with its creation date."""
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")

    task = {
        "title": title.strip(),
        "completed": False,
        "created_at": get_current_time(),
        "completed_at": None
    }

    tasks.append(task)
    return task


def list_tasks():
    """Return all tasks."""
    return tasks


def complete_task(index):
    """Mark a task as completed and record its completion date."""
    if index < 0 or index >= len(tasks):
        raise IndexError("Task not found.")

    task = tasks[index]

    if not task["completed"]:
        task["completed"] = True
        task["completed_at"] = get_current_time()

    return task


def main():
    print("Simple Task Manager")

    while True:
        print("\n1. Add task  2. List tasks  3. Complete task  4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")

            try:
                add_task(title)
                print("Task added successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            if not tasks:
                print("No tasks yet.")

            for number, task in enumerate(list_tasks(), start=1):
                status = "Done" if task["completed"] else "Pending"

                print(f"\n{number}. {task['title']}")
                print(f"   Status: {status}")
                print(f"   Created: {task['created_at']}")
                print(f"   Completed: {task['completed_at'] or 'Not completed'}")

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
