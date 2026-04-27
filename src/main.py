from task import Task
from manager import TaskManager

def main():
    """Main execution loop for the CLI application."""
    print("--- Smart Task Manager ---")
    
    with TaskManager() as manager:
        while True:
            print("\n1. Add Task\n2. View Sorted Tasks\n3. Mark Complete\n4. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                title = input("Task Title: ")
                # Input Validation: Ensuring priority is an integer between 1-5 [cite: 105]
                try:
                    priority = int(input("Priority (1-5): "))
                    if not (1 <= priority <= 5):
                        raise ValueError
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 5.")
                    continue
                
                deadline = input("Deadline (YYYY-MM-DD): ")
                manager.tasks.append(Task(title, priority, deadline))
                print("Task added successfully!")

            elif choice == "2":
                manager.sort_tasks() [cite: 98]
                for idx, task in enumerate(manager.tasks):
                    print(f"{idx + 1}. {task}")

            elif choice == "3":
                idx = int(input("Enter task number to complete: ")) - 1
                if 0 <= idx < len(manager.tasks):
                    manager.tasks[idx].status = "Completed"
                else:
                    print("Invalid task number.")

            elif choice == "4":
                print("Saving and exiting...")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()