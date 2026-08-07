import unittest
from task import Task, UrgentTask, RecurringTask


class TestTask(unittest.TestCase):
    def setUp(self):
        """Create a fresh Task object before each test."""
        self.task = Task("Buy groceries", "high", 30)

    def test_task_creation(self):
        """Test that a Task is created with the correct initial values."""
        self.assertEqual(self.task.name, "Buy groceries")
        self.assertEqual(self.task.get_priority(), "high")
        self.assertEqual(self.task.estimated_time, 30)
        self.assertFalse(self.task.get_is_complete())

    def test_mark_complete(self):
        """Test that mark_complete() sets is_complete to True."""
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())

    def test_set_priority_valid(self):
        """Test that set_priority() updates priority with a valid value."""
        self.task.set_priority("low")
        self.assertEqual(self.task.get_priority(), "low")

    def test_set_priority_invalid(self):
        """Test that set_priority() does not update priority with an invalid value."""
        self.task.set_priority("urgent!")
        self.assertEqual(self.task.get_priority(), "high")

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary with all required fields."""
        result = self.task.to_dict()
        self.assertIn("name", result)
        self.assertIn("priority", result)
        self.assertIn("estimated_time", result)
        self.assertIn("is_complete", result)
        self.assertEqual(result["name"], "Buy groceries")
        self.assertFalse(result["is_complete"])

    def test_from_dict(self):
        """Test that from_dict() recreates a Task from a dictionary correctly."""
        data = {
            "name": "Call doctor",
            "priority": "medium",
            "estimated_time": 15,
            "is_complete": False,
        }
        task = Task.from_dict(data)
        self.assertEqual(task.name, "Call doctor")
        self.assertEqual(task.get_priority(), "medium")
        self.assertFalse(task.get_is_complete())

    def test_str_output(self):
        """Test that __str__ returns a string containing the task name and status."""
        result = str(self.task)
        self.assertIn("Buy groceries", result)
        self.assertIn("Pending", result)


class TestUrgentTask(unittest.TestCase):
    def setUp(self):
        """Create a fresh UrgentTask before each test."""
        self.urgent = UrgentTask("Fix server outage", 5, "2024-12-01")

    def test_urgent_priority_is_always_high(self):
        """Test that UrgentTask always sets priority to high."""
        self.assertEqual(self.urgent.get_priority(), "high")

    def test_urgent_str_contains_label(self):
        """Test that UrgentTask __str__ includes the [URGENT] label."""
        result = str(self.urgent)
        self.assertIn("[URGENT]", result)

    def test_urgent_str_contains_deadline(self):
        """Test that UrgentTask __str__ includes the deadline."""
        result = str(self.urgent)
        self.assertIn("2024-12-01", result)

    def test_urgent_to_dict_includes_type(self):
        """Test that UrgentTask to_dict() includes type UrgentTask and a deadline."""
        result = self.urgent.to_dict()
        self.assertEqual(result["type"], "UrgentTask")
        self.assertIn("deadline", result)


class TestRecurringTask(unittest.TestCase):
    def setUp(self):
        """Create a fresh RecurringTask before each test."""
        self.recurring = RecurringTask("Team standup", "medium", 15, "daily")

    def test_recurring_str_contains_label(self):
        """Test that RecurringTask __str__ includes the [RECURRING label."""
        result = str(self.recurring)
        self.assertIn("[RECURRING", result)

    def test_recurring_to_dict_includes_type(self):
        """Test that RecurringTask to_dict() includes type RecurringTask and a frequency."""
        result = self.recurring.to_dict()
        self.assertEqual(result["type"], "RecurringTask")
        self.assertIn("frequency", result)

    def test_reset(self):
        """Test that reset() sets is_complete back to False."""
        self.recurring.mark_complete()
        self.assertTrue(self.recurring.get_is_complete())
        self.recurring.reset()
        self.assertFalse(self.recurring.get_is_complete())


if __name__ == "__main__":
    unittest.main()