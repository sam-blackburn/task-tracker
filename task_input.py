# STEP 1:
#   Task Tracker Script
#   Author: Sam Blackburn
#   Description: Collect task details from user and print summary.
# STEP 2:
print("Welcome to Task Tracker!")
print("Please enter your task details below.")
print()  # blank line 
# STEP 3:
task_name = input("Enter task name: ")
priority = input("Enter priority level (high, medium, low): ")
estimated_time = int(input("Estimated time to complete (in minutes): "))
urgent = input("Is this task urgent? (yes/no): ")
# STEP 4:
print()  # blank line 
print("Task Summary")
print("Task:", task_name)
print("Priority:", priority)
print("Estimated Time:", estimated_time, "minutes")
print("Urgent:", urgent)
# STEP 5:
# DUMMY DATA TYPES NOT USED IN SCRIPT (BOOLEAN & FLOAT)
incomplete = False  #(T OR F,0 OR 1)
fail_rate = 0.0 # DECIMAL NUMBER
