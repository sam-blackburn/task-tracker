# Task Tracker 
# Author: Sam Blackburn
# Description: A function-based version of the Task Tracker
#              priority checker. Same behaviour, reorganised
#              into reusable functions.

# ---- Global variables: defined outside all functions, readable anywhere ----
APP_NAME = "Task Tracker"   # global variable: the app's name
APP_VERSION = "1.0"         # global variable: the current version number

def greet_user():
    """Print welcome message when program starts.

    Takes no parameters and returns nothing.
    """
    # LOCAL variable - only exists inside greet_user()
    banner = "=" * 40
    print(banner)
    # GLOBAL variables, read here
    print(f"Welcome to {APP_NAME} (version {APP_VERSION})")
    print("Enter your tasks to check their priority.")
    print(banner)
    print()

def get_task_input():
    """Collect a task name from the user, rejecting empty input.

    Keeps asking until the user types a non-empty task name (or 'quit').

    Returns:
        str: the task name the user typed, or 'quit' to stop the program.
    """
    task_name = input("Enter a task name (or type 'quit' to stop): ")

    # len(task_name) == 0 is True when the user presses Enter without typing.
    # Keep asking until they type something.
    while len(task_name) == 0:
        print("Task name cannot be empty. Please try again.")
        task_name = input("Enter a task name (or type 'quit' to stop): ")

    return task_name

def get_priority_input():
    """Collect priority level from user.

    Returns:
        str: the priority the user typed (expected: high, medium, or low).
    """
    priority = input("Enter priority (high, medium, low): ")
    return priority

def check_priority(priority="low"):  # default "low": unspecified task is treated as low urgency
    """Return a message describing how urgent a task is, based on its priority.

    Args:
        priority (str): priority level - high, medium, or low.
                        Defaults to "low" if no argument is passed.

    Returns:
        str: a message telling the user how to handle the task.
    """
    # 'message' is a LOCAL variable 
    if priority == "high":
        message = "Urgent: handle this task first."
    elif priority == "medium":
        message = "Important: schedule this task soon."
    elif priority == "low":
        message = "Low priority: handle when time allows."
    else:
        message = "Priority not recognised. Please enter high, medium, or low."

    return message   # send message back instead of printing it

def run_tracker():
    """Run the Task Tracker.

    Greets the user, then loops asking for tasks and reporting each task's
    priority until the user types 'quit'. Ties all the other functions together.
    """
    greet_user()

    task_name = ""   # local variable; start empty so the loop can begin

    while task_name != "quit":
        task_name = get_task_input()

        if task_name != "quit":
            priority = get_priority_input()
            result = check_priority(priority)   # pass priority in, get message back
            print(result)
            print()

    print("Session ended. Goodbye!")

# Start program 
run_tracker()