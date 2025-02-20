import json
import os

# Dummy credentials for login
DUMMY_EMAIL = "test@example.com"
DUMMY_PASSWORD = "password123"


#Define task Structure
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{self.id}] {self.title} - {status}"


# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def delete_task(self, task_id):
        task_to_delete = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"Task {task_id} deleted.")
        else:
            print(f"No task found with ID {task_id}.")

    def mark_task_as_complete(self, task_id):
        task_to_complete = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_complete:
            task_to_complete.completed = True
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"No task found with ID {task_id}.")

#File Handling
    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)
        print("Tasks saved to tasks.json.")

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(task_id=task['id'], title=task['title'], completed=task['completed']) for task in tasks_data]
            print("Tasks loaded from tasks.json.")


# Login
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False



# Main function for CLI
def main():
    if not login():
        return

    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_task_as_complete(task_id)
        elif choice == '5':
            manager.save_tasks()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()