# Task Tracker - Priority Checker
# Author: Sam Blackburn
# Description: Asks for tasks in a loop and reports each task's 
#              priority until user types "quit".

print("Welcome to Task Tracker Priority Checker")
print("Enter your tasks one at a time to check their priority.")
print()   # blank line

user_input = ""   # holds task name

# Keep looping until user types "quit" for the task name
while user_input != "quit":
    user_input = input("Enter a task name (or type 'quit' to stop): ")

    # Only ask for priority if user did NOT quit
    if user_input != "quit":
        # check the task name has more than 0 characters.
        if len(user_input) > 0:
            priority = input("Enter priority (high, medium, low): ")
            # Print message depending on the priority entered
            if priority == "high":
                print("Urgent: handle this task first.")
            elif priority == "medium":
                print("Important: schedule this task soon.")
            elif priority == "low":
                print("Low priority: handle when time allows.")
            else:
                print("Priority not recognized. Please enter high, medium, or low.")
        else:
            print("Task name cannot be empty. Please try again.")

        print()   # blank line 

print("Session ended. Goodbye!")