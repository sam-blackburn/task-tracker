# Task Manager - Week 2 main project file
# Author: Sam Blackburn
# Description: A CLI Task Manager supporting multiple task types (Task,
#              UrgentTask, RecurringTask) via inheritance and polymorphism,
#              with JSON persistence and error handling.

import json
from task import Task, UrgentTask, RecurringTask, task_from_dict

# TASKS_FILE is the name of the JSON file where tasks are saved between sessions.
TASKS_FILE = "tasks.json"

# 'tasks' is a global list that holds every task object while the program runs.
tasks = []


def add_task(name, priority, estimated_time):
    """Create a basic Task object and append it to the global tasks list."""
    task = Task(name, priority, estimated_time)
    tasks.append(task)
    print(f"Task added: {name}")


def add_urgent_task():
    """Collect input for an urgent task and add an UrgentTask to the list.

    Urgent tasks are always high priority, so no priority is asked.
    """
    name = input("Task name: ")
    try:
        estimated_time = int(input("Estimated time in minutes: "))
    except ValueError:
        print("Please enter a whole number for estimated time.")
        return
    deadline = input("Deadline (e.g. 2024-12-01): ")
    task = UrgentTask(name, estimated_time, deadline)
    tasks.append(task)
    print(f"Urgent task added: {name}")


def add_recurring_task():
    """Collect input for a recurring task and add a RecurringTask to the list."""
    name = input("Task name: ")
    priority = input("Priority (high, medium, low): ")
    try:
        estimated_time = int(input("Estimated time in minutes: "))
    except ValueError:
        print("Please enter a whole number for estimated time.")
        return
    frequency = input("Frequency (e.g. daily, weekly): ")
    task = RecurringTask(name, priority, estimated_time, frequency)
    tasks.append(task)
    print(f"Recurring task added: {name}")


def view_tasks():
    """Print every task with its number, using each task's own __str__."""
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for i in range(len(tasks)):
        task = tasks[i]
        print(f"{i + 1}. {task}")   # polymorphism: each type prints itself


def complete_task(index):
    """Mark the task at the given index as complete."""
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return
    tasks[index].mark_complete()
    print(f"Task marked complete: {tasks[index].name}")


def delete_task(index):
    """Remove the task at the given index from the tasks list."""
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return
    removed = tasks.pop(index)
    print(f"Task deleted: {removed.name}")


def save_tasks():
    """Save the current tasks list to the JSON file (each task via to_dict())."""
    with open(TASKS_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
    print("Tasks saved.")


def load_tasks():
    """Load tasks from the JSON file, rebuilding the correct task subclass."""
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [task_from_dict(t) for t in json.load(file)]
        print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def run_manager():
    """Main loop for the Task Manager with multiple task types, file
    persistence, and error handling."""
    load_tasks()
    print("Welcome to the Task Manager!")
    print()

    while True:
        print("Options: add | add-urgent | add-recurring | view | complete | delete | save | quit")
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

        elif choice == "add-urgent":
            add_urgent_task()

        elif choice == "add-recurring":
            add_recurring_task()

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
            print("Option not recognized. Please choose add, add-urgent, add-recurring, view, complete, delete, save, or quit.")

        print()


# Start the program
run_manager()