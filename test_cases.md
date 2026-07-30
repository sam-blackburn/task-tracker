# Test Cases for task_priority.py

These test cases document the expected behaviour of the Task Tracker
Priority Checker. Each test is run by starting the script with `python task_priority.py`.

| Test Case ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-01 | Valid input: a high-priority task is entered | Task name: `Buy groceries` <br> Priority: `high` | `Urgent: handle this task first.` |
| TC-02 | Valid input: a low-priority task is entered | Task name: `Water plants` <br> Priority: `low` | `Low priority: handle when time allows.` |
| TC-03 | Edge case: task name left blank (Enter pressed with no text) | Task name: *(empty — just press Enter)* | `Task name cannot be empty. Please try again.` and the priority question is never asked |
| TC-04 | Invalid input: an unrecognised priority word is entered | Task name: `Call doctor` <br> Priority: `whenever` | `Priority not recognized. Please enter high, medium, or low.` |
| TC-05 | Edge/invalid: correct word but wrong capitalisation (tests case sensitivity) | Task name: `Email boss` <br> Priority: `High` | `Priority not recognized. Please enter high, medium, or low.` — because `High` does not exactly equal `high` |