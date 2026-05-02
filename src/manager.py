"""TaskManager class for CSV persistence and task sorting.

This module provides the TaskManager context manager that automatically loads
tasks from a CSV file on entry and saves them on exit. It also includes a
sorting algorithm to order tasks by priority.
"""

import csv
import os
from task import Task

class TaskManager:
    """Manages tasks with data stored in the data/ directory."""

    def __init__(self, filename="data/tasks.csv"):
        self.filename = filename
        self.tasks = []
        
        if not os.path.exists("data"):
            os.makedirs("data")

    def __enter__(self):
        """Loads tasks from the data/tasks.csv file on program start."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tasks.append(Task(
                        row['title'], 
                        int(row['priority']),  # ensure int
                        row['deadline'], 
                        row['status']
                    ))
            # Auto-load confirmation message (persistence check)
            print(f"✅ Loaded {len(self.tasks)} existing task(s) from {self.filename}")
        except FileNotFoundError:
            # No saved file yet – fresh start
            print(f"📂 No previous save found. Starting with an empty task list.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Saves tasks to the CSV file when exiting the 'with' block."""
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['title', 'priority', 'deadline', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({
                    'title': task.title,
                    'priority': task.priority,
                    'deadline': task.deadline,
                    'status': task.status
                })
        print(f"💾 Saved {len(self.tasks)} task(s) to {self.filename}")

    def sort_tasks(self):
        """
        Algorithm: Sorts tasks by priority (Level 5 first).
        """
        self.tasks.sort(key=lambda x: x.priority, reverse=True)