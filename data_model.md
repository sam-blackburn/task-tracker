# Task Manager Data Model

This document describes the data model used by `task_manager.py` and maps it
back to the requirements document.

## Section 1: Task Dictionary Structure

Each task is stored as a dictionary with the following four fields:

| Field Name | Data Type | Description | Default Value |
|---|---|---|---|
| `name` | str | The name of the task | None (entered by the user when the task is added) |
| `priority` | str | The priority level of the task (high, medium, or low) | None (entered by the user) |
| `is_complete` | bool | Whether the task has been marked complete | `False` |
| `estimated_time` | int | Estimated time to complete the task, in minutes | None (entered by the user) |

## Section 2: Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|---|---|---|
| The system shall allow the user to add a task | `add_task()`; `name`, `priority`, `estimated_time` fields | Builds a new task dictionary from the four fields and appends it to the `tasks` list |
| The system shall allow the user to view all tasks | `view_tasks()` | Loops through the `tasks` list and prints each task's number, name, priority, status, and estimated time |
| The system shall allow the user to mark a task as complete | `complete_task()`; `is_complete` field | Sets the selected task's `is_complete` field from `False` to `True` |
| The system shall allow the user to delete a task | `delete_task()` | Removes the selected task from the `tasks` list using `pop()` |

Not yet implemented (planned for later in Week 2):

- **Edit / update a task** — no function yet; will modify fields of an existing task dictionary.
- **Persist tasks across sessions** — currently in memory only; JSON file storage is planned for later.

## Section 3: Assumptions

- Tasks are stored **in memory only** (in the global `tasks` list). They are not saved to a file yet, so all tasks are lost when the program closes.
- `estimated_time` is always entered as a **whole number** of minutes (converted with `int()`).
- `priority` is expected to be **high, medium, or low** — this is assumed but not yet enforced by the code.
- Task numbers shown to the user start at **1**, while the underlying list is **zero-indexed** (the code subtracts 1 to convert).