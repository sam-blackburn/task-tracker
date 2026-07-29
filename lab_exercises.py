# ============================================================
# Task Tracker Project - 10 Python Lab Exercises (plus bonus)
# Author: Sam Blackburn
# Description: Combined script that runs all 
#              exercises, each with a header line.
# Topics: comments, print(), variables, data types, input()
# ============================================================

print("========== EXERCISE 1: Welcome to Task Tracker ==========")
print("=============================")
print("  TASK TRACKER")
print("=============================")
print("Welcome to Task Tracker")
print("Student: Sam Blackburn")
print("Date: 29-07-2026")   # date hardcoded 
print()   # blank line 

print("========== EXERCISE 2: Create a Task ==========")
task_id = 101                      # int
task_name = "Design Task Page"     # str
priority = "High"                  # str
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Priority:", priority)
print()

print("========== EXERCISE 3: Display Data Types ==========")
task_name = "Design Homepage"      # str  
task_id = 201                      # int  
estimated_hours = 5.5              # float 
task_completed = False             # bool 
print("Task Name:", task_name)
print(type(task_name))
print("Task ID:", task_id)
print(type(task_id))
print("Estimated Hours:", estimated_hours)
print(type(estimated_hours))
print("Task Completed:", task_completed)
print(type(task_completed))
print()

print("========== EXERCISE 4: Employee Task Assignment ==========")
employee_name = input("Enter Employee Name: ")
task_name = input("Enter Task Name: ")
print("Employee:", employee_name)
print("Assigned Task:", task_name)
print()

print("========== EXERCISE 5: Task Information Form ==========")
task_id = input("Enter Task ID: ")
task_name = input("Enter Task Name: ")
department = input("Enter Department: ")
estimated_hours = input("Enter Estimated Hours: ")
print("=========================")
print("TASK INFORMATION")
print("=========================")
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Department:", department)
print("Estimated Hours:", estimated_hours)
print()

print("========== EXERCISE 6: Daily Work Log ==========")
employee_name = "Paul"             # str
tasks_completed = 4                # int
working_hours = 8.5                # float
is_attendance_marked = True        # bool
print("Employee:", employee_name)
print("Tasks Completed:", tasks_completed)
print("Working Hours:", working_hours)
print("Attendance:", is_attendance_marked)
print()

print("========== EXERCISE 7: Project Registration ==========")
project_name = input("Enter Project Name: ")
team_leader = input("Enter Team Leader: ")
team_members = int(input("Enter Number of Team Members: ")) # make int
print("Project Name:", project_name)
print("Team Leader:", team_leader)
print("Team Members:", team_members)
print()

print("========== EXERCISE 8: Task Summary Report ==========")
task_name = "Testing Module"       # str
assigned_employee = "Jeffery"      # str
priority = "Medium"                # str
due_date = "30-07-2026"            # str
status = "Pending"                 # str
print("==========================")
print("TASK SUMMARY")
print("==========================")
print("Task Name:", task_name)
print("Assigned To:", assigned_employee)
print("Priority:", priority)
print("Due Date:", due_date)
print("Status:", status)
print()

print("========== EXERCISE 9: User Input and Data Types ==========")
task_id = int(input("Enter Task ID: "))                     # make int
estimated_hours = float(input("Enter Estimated Hours: "))   # make float
print("Task ID:", task_id)
print(type(task_id))
print("Estimated Hours:", estimated_hours)
print(type(estimated_hours))
print()

print("========== EXERCISE 10: Mini Task Tracker Registration ==========")
task_id = input("Enter Task ID: ")
task_name = input("Enter Task Name: ")
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
priority = input("Enter Priority: ")
estimated_hours = float(input("Enter Estimated Hours: "))       # make float
completed_status = input("Enter Completed Status (True/False): ")  # kept as text
print("====================================")
print(" TASK TRACKER REPORT")
print("====================================")
print("Task ID :", task_id)
print("Task Name :", task_name)
print("Employee Name :", employee_name)
print("Department :", department)
print("Priority :", priority)
print("Estimated Hours :", estimated_hours)
print("Completed :", completed_status)
print("====================================")

print("========== BONUS CHALLENGE: Student Task Tracker ==========")
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
course = input("Enter Course: ")
assignment_name = input("Enter Assignment Name: ")
assignment_deadline = input("Enter Assignment Deadline (DD-MM-YYYY): ")
estimated_time = float(input("Enter Estimated Time (Hours): "))       # make float
assignment_submitted = input("Is the Assignment Submitted? (True/False): ")  # kept as text

print() 
print("========================================")
print("       STUDENT TASK TRACKER REPORT")
print("========================================")
print("Student ID      :", student_id)
print("Student Name    :", student_name)
print("Course          :", course)
print("Assignment Name :", assignment_name)
print("Deadline        :", assignment_deadline)
print("Estimated Time  :", estimated_time, "hours")
print("Submitted       :", assignment_submitted)
print("========================================")