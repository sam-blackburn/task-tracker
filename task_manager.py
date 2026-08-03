# Task Manager - Week 2 main project file
# Author: Sam Blackburn
# Description: A CLI Task Manager that stores tasks as a list of dictionaries
#              and supports adding, viewing, completing, and deleting tasks.
# 'tasks' is a global list that holds every task (each task is a dictionary)
# for as long as the program is running.
tasks = []


def add_task(name, priority, estimated_time):
    """Create task dictionary and append it to global tasks list.

    Args:
        name (str): name of task.
        priority (str): priority level (high, medium, or low).
        estimated_time (int): estimated minutes to complete the task.

    Prints a confirmation message. Returns nothing.
    """
    task = {
        "name": name,
        "priority": priority,
        "is_complete": False,      # new tasks start as not complete
        "estimated_time": estimated_time,
    }
    tasks.append(task)
    print(f"Task added: {name}")


def view_tasks():
    """Print every task in tasks list with its number and details.

    If list is empty, prints a message saying no tasks were found.
    """
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i in range(len(tasks)):
        task = tasks[i]   # local variable: the dictionary at position i
        # show "Complete" when done, otherwise "Pending"
        status = "Complete" if task["is_complete"] else "Pending"
        print(
            f"{i + 1}. {task['name']}"
            f" | Priority: {task['priority']}"
            f" | Status: {status}"
            f" | Est. Time: {task['estimated_time']} mins"
        )


def complete_task(index):
    """Mark task at the given index as complete.

    Args:
        index (int): zero-based position of the task in tasks list.

    Prints confirmation, or error message if the index is out of range.
    """
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return

    tasks[index]["is_complete"] = True
    print(f"Task marked complete: {tasks[index]['name']}")


def delete_task(index):
    """Remove the task at the given index from tasks list.

    Args:
        index (int): zero-based position of the task in tasks list.

    Prints confirmation with deleted task's name, or an error message
    if index is out of range.
    """
    if index < 0 or index >= len(tasks):
        print("Error: that task number does not exist.")
        return

    removed_task = tasks.pop(index)   # pop() removes and returns task
    print(f"Task deleted: {removed_task['name']}")


def run_manager():
    """Run the main loop of Task Manager.

    Prints welcome message, then repeatedly shows the menu and runs the
    command the user chooses (add, view, complete, delete, quit) until they
    type 'quit'.
    """
    print("Welcome to the Task Manager!")

    while True:
        print()
        print("Options: add | view | complete | delete | quit")
        command = input("Choose an option: ")
        print()

        if command == "add":
            name = input("Task name: ")
            priority = input("Priority (high, medium, low): ")
            estimated_time = int(input("Estimated time in minutes: "))  # text -> int
            add_task(name, priority, estimated_time)

        elif command == "view":
            view_tasks()

        elif command == "complete":
            view_tasks()   # show list first so user can pick a number
            task_number = int(input("Enter task number to mark complete: "))
            # subtract 1 to get the real index.
            complete_task(task_number - 1)

        elif command == "delete":
            view_tasks()   # show list first so the user can pick a number
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number - 1)   # convert 1-based number to zero-based index

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Unrecognized option. Please type add, view, complete, delete, or quit.")


# Start the program
run_manager()