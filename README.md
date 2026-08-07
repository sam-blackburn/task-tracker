# Task Manager

A command-line Task Manager built in Python as part of the SDLC and Python
Foundations program. It lets a user add, view, complete, and delete tasks across
three task types: standard, urgent, and recurring; and saves everything to a
JSON file so tasks persist between sessions. It uses an object-oriented design: a
`Task` base class with encapsulated data, plus `UrgentTask` and `RecurringTask`
subclasses (inheritance and polymorphism), using only the Python standard library
(`json`, `unittest`).

## How to Run
1. Clone the repository:
`git clone https://github.com/sam-blackburn/task-tracker.git`
2. Navigate to the project folder:
`cd task-tracker`
3. Run the Task Manager (use `python3` on macOS/Linux):
`python task_manager.py`


## Features
- Add standard, urgent, and recurring tasks
- View all tasks with priority, completion status, and estimated time
- Mark tasks as complete
- Delete tasks
- Save and load tasks automatically using JSON file persistence
- Graceful handling of unrecognized menu options and non-numeric number input
- Object-oriented design using a Task class with encapsulation, inheritance, and polymorphism

## Project Structure
- README.md: Project overview, setup, features, and known issues (this file).
- task.py: The Task base class, UrgentTask and RecurringTask subclasses, and the task_from_dict factory.
- task_manager.py: The main menu-driven program with file persistence and error handling.
- test_task.py: Unit tests for the Task class and its subclasses (unittest).
- test_results.txt: Captured output from the passing unit test run.
- code_review.md: Structured self-review and release readiness checklist.
- bug_report.md: Documented known bugs with reproduction steps.
- data_model.md: Data model documentation and requirements mapping.
- tasks.json: Saved task data (auto-generated on first save).
- task_input.py: Week 1 script collecting basic task info using variables and I/O.
- task_priority.py: Week 1 script adding priority logic with conditionals and a loop.
- task_tracker.py: Week 1 function-based version of the tracker.
- test_cases.md: Week 1 manual QA test cases for task_priority.py.

## Known Bugs and Limitations
- Priorities are not validated when adding a task; any value (including "urgent!" or a miscapitalised "High") is accepted and stored. See BUG-01.
- Urgent task deadlines are not validated as real dates; any text is accepted. See BUG-02.
- `set_priority()` is case-sensitive: "High" is treated as invalid because it does not exactly match "high".
- Recurring tasks do not reset automatically, and there is currently no menu option to trigger `reset()` while the program is running.

## Future Improvements
- Validate priority at creation by routing the constructor through `set_priority()`, and make the check case-insensitive.
- Add date validation for urgent task deadlines (e.g enforce a DD-MM-YYYY format).
- Add a menu option to reset a recurring task for its next cycle.
- Add a search or filter feature to find tasks by priority, name or completion status.