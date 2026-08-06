# task.py
# Author: Sam Blackburn
# Description: Defines the Task class and its subclasses (UrgentTask,
#              RecurringTask) for the Task Manager, plus a factory function
#              to rebuild the correct task type from saved JSON data.


class Task:
    def __init__(self, name, priority, estimated_time):
        """Initialize a new Task with a name, priority, estimated time, and a
        completion status that starts as False."""
        self.name = name                       # regular (public) attribute
        self.__priority = priority             # private attribute
        self.estimated_time = estimated_time   # regular (public) attribute
        self.__is_complete = False             # private attribute, defaults to F

    def get_priority(self):
        """Return the task's priority level."""
        return self.__priority

    def set_priority(self, priority):
        """Update the priority, but only if it is high, medium, or low."""
        if priority in ["high", "medium", "low"]:
            self.__priority = priority
        else:
            print("Invalid priority. Choose high, medium, or low.")

    def get_is_complete(self):
        """Return the task's completion status (True or False)."""
        return self.__is_complete

    def mark_complete(self):
        """Mark the task as complete by setting the completion status to True."""
        self.__is_complete = True

    def reset(self):
        """Reset the task's completion status back to False."""
        self.__is_complete = False

    def to_dict(self):
        """Convert the Task object to a plain dictionary for JSON saving.

        Includes a 'type' field so the correct class can be rebuilt on load.
        """
        return {
            "type": "Task",
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete,
        }

    @classmethod
    def from_dict(cls, data):
        """Create and return Task object from dictionary."""
        task = cls(data["name"], data["priority"], data["estimated_time"])
        if data["is_complete"]:
            task.mark_complete()
        return task

    def __str__(self):
        """Return a readable string representation of the task."""
        status = "Done" if self.__is_complete else "Pending"
        return f"{self.name} | Priority: {self.__priority} | Status: {status} | Est. Time: {self.estimated_time} mins"


class UrgentTask(Task):
    def __init__(self, name, estimated_time, deadline):
        """Initialize an UrgentTask. Urgent tasks are always high priority, so
        priority is set automatically and a deadline is stored."""
        super().__init__(name, "high", estimated_time)
        self.deadline = deadline   # regular attribute unique to UrgentTask

    def __str__(self):
        """Override Task's __str__ to add an [URGENT] label and the deadline."""
        status = "Done" if self.get_is_complete() else "Pending"
        return f"[URGENT] {self.name} | Status: {status} | Est. Time: {self.estimated_time} mins | Deadline: {self.deadline}"

    def to_dict(self):
        """Override to_dict() to record the type and the deadline."""
        data = super().to_dict()
        data["type"] = "UrgentTask"
        data["deadline"] = self.deadline
        return data


class RecurringTask(Task):
    def __init__(self, name, priority, estimated_time, frequency):
        """Initialize a RecurringTask with a repeating frequency (e.g. daily)."""
        super().__init__(name, priority, estimated_time)
        self.frequency = frequency   # regular attribute unique to RecurringTask

    def __str__(self):
        """Override Task's __str__ to add a [RECURRING: frequency] label."""
        status = "Done" if self.get_is_complete() else "Pending"
        return f"[RECURRING: {self.frequency}] {self.name} | Priority: {self.get_priority()} | Status: {status} | Est. Time: {self.estimated_time} mins"

    def reset(self):
        """Reset the task to incomplete so it can run again next cycle."""
        super().reset()   # parent handles the private attribute cleanly
        print(f"Task reset for next {self.frequency}: {self.name}")

    def to_dict(self):
        """Override to_dict() to record the type and the frequency."""
        data = super().to_dict()
        data["type"] = "RecurringTask"
        data["frequency"] = self.frequency
        return data


def task_from_dict(data):
    """Create the correct Task (or subclass) object from a saved dictionary.

    Reads the 'type' field and builds an UrgentTask, RecurringTask, or a base
    Task accordingly, restoring completion status.
    """
    task_type = data.get("type", "Task")
    if task_type == "UrgentTask":
        task = UrgentTask(data["name"], data["estimated_time"], data["deadline"])
    elif task_type == "RecurringTask":
        task = RecurringTask(data["name"], data["priority"], data["estimated_time"], data["frequency"])
    else:
        return Task.from_dict(data)

    # restore completion status for the subclasses too
    if data.get("is_complete"):
        task.mark_complete()
    return task


if __name__ == "__main__":
    demo_tasks = [
        Task("Buy groceries", "low", 30),
        UrgentTask("Fix server outage", 5, "2024-12-01"),
        RecurringTask("Team standup", "medium", 15, "daily"),
    ]

    print("--- Polymorphism Demo ---")
    for task in demo_tasks:
        print(task)
        print("Is a Task instance:", isinstance(task, Task))
        print()