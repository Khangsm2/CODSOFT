class ToDoList:
    """A simple To-Do List manager."""
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully.")

    def view_tasks(self):
        """View all tasks in the list."""
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']} - {task['status']}")
        print()

    def update_task(self, index):
        """Update the status of a task."""
        try:
            if 0 < index <= len(self.tasks):
                new_status = input("Enter new status (Pending/In Progress/Completed): ").strip()
                if new_status in ["Pending", "In Progress", "Completed"]:
                    self.tasks[index - 1]["status"] = new_status
                    print("Task status updated successfully.")
                else:
                    print("Invalid status. Please use 'Pending', 'In Progress', or 'Completed'.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

    def delete_task(self, index):
        """Delete a task from the list."""
        try:
            if 0 < index <= len(self.tasks):
                self.tasks.pop(index - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")

def main():
    to_do_list = ToDoList()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task = input("Enter the task description: ")
                to_do_list.add_task(task)
            elif choice == 2:
                to_do_list.view_tasks()
            elif choice == 3:
                to_do_list.view_tasks()
                index = int(input("Enter the task number to update: "))
                to_do_list.update_task(index)
            elif choice == 4:
                to_do_list.view_tasks()
                index = int(input("Enter the task number to delete: "))
                to_do_list.delete_task(index)
            elif choice == 5:
                print("Exiting To-Do List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
