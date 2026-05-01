"""Task class representing a single to‑do item.

This module defines the Task class with attributes for title, priority,
deadline, and status. It also provides a string representation for CLI display.
"""

class Task:
    """Represents a single to-do item with priority and status."""

    def __init__(self, title, priority, deadline, status="Pending"):
        """
        Initializes a Task object.

        Args:
            title (str): The name of the task.
            priority (int): Priority level from 1 (low) to 5 (high).
            deadline (str): The due date.
            status (str): The current state of the task.
        """
        self.title = title
        self.priority = int(priority)
        self.deadline = deadline
        self.status = status

    def __str__(self):
        """Returns a formatted string for CLI display."""
        return f"[{self.status}] P{self.priority} | {self.title} (Due: {self.deadline})"