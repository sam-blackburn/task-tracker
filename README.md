# Task Tracker

**Author:** Sam Blackburn

A command-line Task Tracker application. It will let a user 
add, view, update, complete, and delete tasks, with all tasks 
saved locally on a JSON file, persisting between sessions.

## Project Structure

- task_input.py: Collects basic task information from the user using variables and input/output.
- task_priority.py: Adds priority logic using conditionals and a while loop.
- task_tracker.py: Refactored main version using functions, scope, docstrings, and a default parameter.
- test_cases.md: Documents five QA test cases for task_priority.py.
- lab_exercises.py: Standalone practice exercises covering comments, print(), variables, data types, and input().
- task_manager.py: Week 2 main file; stores tasks as a list of dictionaries with add, view, complete, and delete functions.
- data_model.md: Documents the task dictionary structure and maps each field and function back to the requirements doc.

## Week 2 Progress

Adding file persistence solved the problem of losing every task when the program
closed. Before this the task list lived only in memory, so all tasks
disappeared the moment the program ended; now they are saved to `tasks.json` and
reloaded on the next run. If I did not catch the `FileNotFoundError` when loading,
the program would crash on its very first run — because `tasks.json` does not
exist yet — before the user could add a single task. Catching that error lets the
program start cleanly with an empty list instead, tying directly to the QA
mindset from Week 1 Day 4: where a QA engineer anticipates edge cases and invalid input
(missing file, non-numeric) and makes sure the program handles them
gracefully rather than crashing.