# Bug Report: Task Manager

## BUG-01

**Description:** When adding a standard task, the priority value is not validated. The `Task` constructor stores whatever is entered directly, so invalid or miscapitalised values (for example "urgent!" or "High") are accepted and saved as-is instead of being limited to high, medium, or low.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Choose `add`
3. Enter "urgent!" as the priority level
4. Choose `view`

**Expected Behavior:** The priority is rejected or corrected, and only "high", "medium", or "low" are stored.

**Actual Behavior:** The task is created with the priority stored exactly as typed ("urgent!"), with no error or validation.

## BUG-02

**Description:** The deadline entered for an urgent task is not validated as a real date. Any text is accepted and stored.

**Steps to Reproduce:**
1. Run `task_manager.py`
2. Choose `add-urgent`
3. Enter a task name and an estimated time
4. Enter "dummy" as the deadline
5. Choose `view`

**Expected Behavior:** The program rejects the invalid deadline or warns that it is not a valid date (for example, DD-MM-YYYY).

**Actual Behavior:** The urgent task is created with the deadline stored as "dummy" and displayed as-is.