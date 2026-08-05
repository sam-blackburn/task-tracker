# Task Manager - Week 2 main project file
# Author: Sam Blackburn
# Description: A CLI Task Manager that stores tasks as Task objects, saves them
#              to a JSON file, and handles invalid input gracefully.

import json
from task import Task   # Task class from task.py

# TASKS_FILE is the name of the JSON file where tasks are saved between sessions.
TASKS_FILE = "tasks.json"

# 'tasks' is a global list that holds every task (each item is a Task object)
# for as long as the program is running.
tasks = []


def add_task(name, priority, estimated_time):
    """Create a Task object and append it to the global tasks list.

    Args:
        name (str): the name of the task.
        priority (str): the priority level (high, medium, or low).
        estimated_time (int): estimated minutes to complete the task.

    Prints a confirmation message.
    """
    task = Task(name, priority, estimated_time)   # a Task object, not a dictionary
    tasks.append(task)
    print(f"Task added: {name}")


def view_tasks():
    """Print every task in the tasks list with its number.

    Uses each Task's __str__ method. If the list is empty, prints a message.
    """
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i in range(len(tasks)):
        task = tasks[i]
        # printing a Task object automatically uses its __str__ method
        print(f"{i + 1}. {task}")


def complete_task(index):
    """Mark the task at the given index as complete.

    Args:
        index (int): the zero-based position of the task in the tasks list.

    Prints a confirmation, or an error message if the index is out of range.
    """
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return

    tasks[index].mark_complete()   # use the Task method instead of setting a dict key
    print(f"Task marked complete: {tasks[index].name}")


def delete_task(index):
    """Remove the task at the given index from the tasks list.

    Args:
        index (int): the zero-based position of the task in the tasks list.

    Prints a confirmation with the deleted task's name, or an error message
    if the index is out of range.
    """
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return

    removed = tasks.pop(index)               # pop() returns the Task object
    print(f"Task deleted: {removed.name}")   # use the object's .name attribute


def save_tasks():
    """Save the current tasks list to the JSON file (TASKS_FILE).

    Each Task is converted to a plain dictionary with to_dict() first.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
    print("Tasks saved.")


def load_tasks():
    """Load tasks from the JSON file into the global tasks list.

    Each saved dictionary is rebuilt into a Task object with Task.from_dict().
    Starts with an empty list if the file is missing or corrupted.
    """
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [Task.from_dict(t) for t in json.load(file)]
        print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def run_manager():
    """Main loop for the Task Manager with file persistence and error handling.

    Loads saved tasks, then repeatedly runs the command the user chooses
    (add, view, complete, delete, save, quit) until they type 'quit', saving
    automatically on exit.
    """
    load_tasks()
    print("Welcome to the Task Manager!")
    print()

    while True:
        print("Options: add | view | complete | delete | save | quit")
        choice = input("Choose an option: ").strip().lower()
        print()

        if choice == "add":
            name = input("Task name: ")
            priority = input("Priority (high, medium, low): ")
            try:
                estimated_time = int(input("Estimated time in minutes: "))
            except ValueError:
                print("Please enter a whole number for estimated time.")
                print()
                continue
            add_task(name, priority, estimated_time)

        elif choice == "view":
            view_tasks()

        elif choice == "complete":
            view_tasks()
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == "delete":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == "save":
            save_tasks()

        elif choice == "quit":
            save_tasks()
            print("Goodbye!")
            break

        else:
            print("Option not recognized. Please choose add, view, complete, delete, save, or quit.")

        print()


# Start the program
run_manager()