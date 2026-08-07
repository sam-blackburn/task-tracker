# Code Review: Task Manager

**Reviewer:** Sam Blackburn
**Project:** Task Manager v1.0

## Code Quality
- [x] All functions and methods have docstrings; every function, method, and subclass override has one.
- [x] No unused variables or commented-out code blocks remain - only comments; no dead code.
- [x] Variable and function names are descriptive and follow Python conventions - `snake_case` functions/variables, `PascalCase` classes (`Task`, `UrgentTask`, `RecurringTask`), `UPPER_CASE` constant (`TASKS_FILE`).

## Correctness
- [x] Adding a task creates the correct object type and appends it - `add` / `add-urgent` / `add-recurring` create `Task` / `UrgentTask` / `RecurringTask`.
- [x] Viewing tasks displays all fields including status - `view_tasks()` prints each task number plus its `__str__` output.
- [x] Completing a task correctly updates `is_complete` - `complete_task()` calls `mark_complete()`; covered by `test_mark_complete`.
- [x] Deleting a task removes it and prints the correct name - `delete_task()` uses `pop()` and prints `removed.name`.
- [x] Saving writes a valid `tasks.json` - `save_tasks()` dumps `[task.to_dict() for task in tasks]` with `indent=4`.
- [x] Loading restores all task types using `task_from_dict` - verified with a save/load round-trip; types, deadline, frequency, and completion status all restored.

## Edge Cases
- [x] Empty task list handled in `view_tasks()` - prints "No tasks found."
- [~] Invalid priority rejected by `set_priority()` - `set_priority()` does reject invalid values. **Finding:** the `add` flow creates tasks via the constructor, which stores priority directly and never calls `set_priority()`, so invalid priorities can still enter at creation. Logged as **BUG-01**.
- [x] Non-numeric estimated time caught with `ValueError` - all three add functions wrap `int(input())` in `try/except ValueError`.
- [x] Out-of-range task numbers handled in `complete_task()` and `delete_task()` - both check `index < 0 or index >= len(tasks)` before acting.

## Documentation
- [x] README complete with all required sections.
- [x] Project Structure lists every file.
- [x] Known bugs documented in `bug_report.md` and summarised in the README.

## One Improvement You Made
While reviewing whether loading restores every task type correctly, I found that the `task_from_dict()` factory rebuilt `UrgentTask` and `RecurringTask` objects but never restored their completion status, so a task saved as complete would reload as pending. I fixed it by adding a check that calls `mark_complete()` on the rebuilt object whenever the saved dictionary has `is_complete` set to `True`. I confirmed the fix with a save-and-reload test: a completed urgent task now correctly reloads showing "Done."

## Release Readiness Checklist: Task Manager v1.0

### Code Quality
- [x] All functions and methods have docstrings
- [x] No unused variables or commented-out code blocks remain
- [x] Variable and function names are descriptive

### Testing
- [x] All unit tests pass with zero failures (14 tests, OK)
- [~] Edge cases are covered in tests - invalid priority is unit-tested; empty-list and out-of-range handling are verified manually but not yet unit-tested
- [x] All three task types have been manually tested end to end

### Documentation
- [x] README is complete and up to date
- [x] Project Structure section lists all files
- [x] Known bugs are documented in bug_report.md
- [x] Future improvements are listed

### Version Control
- [x] All changes committed with clear messages
- [x] Repository is public and accessible

### File Persistence
- [x] tasks.json is generated correctly on save
- [x] Tasks reload correctly on restart for all three task types