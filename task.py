# task.py
# Author: Sam Blackburn
# Description: Defines the Task class used by the Task Manager. A Task bundles
#              its data (name, priority, estimated time, completion status) with
#              the behaviour that operates on it, using encapsulation to protect
#              the private attributes.


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

    def to_dict(self):
        """Convert the Task object to a plain dictionary for JSON saving."""
        return {
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete,
        }

    @classmethod
    def from_dict(cls, data):
        """Create and return a Task object from a dictionary (used when loading
        from JSON)."""
        task = cls(data["name"], data["priority"], data["estimated_time"])
        if data["is_complete"]:
            task.mark_complete()
        return task

    def __str__(self):
        """Return a readable string representation of the task."""
        status = "Done" if self.__is_complete else "Pending"
        return f"{self.name} | Priority: {self.__priority} | Status: {status} | Est. Time: {self.estimated_time} mins"