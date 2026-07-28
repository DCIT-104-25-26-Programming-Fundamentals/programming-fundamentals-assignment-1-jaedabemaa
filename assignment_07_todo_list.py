# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

tasks=[]
def add_task():
    """prompt the user for a task description, add it to the  list, and confirm."""
    description = input("Enter task:").strip()
    if description == "":
        print("Task cannot be empty. Nothing was added.")
        return

    tasks.append(description)
    print(f'Task addeed: "{description}"')
    def view_tasks():
        """Display all tasks currently in the list, numbered from 1."""
        if not tasks:
            print("Your to-do list is empty. Add a task to get started!")
            return
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            def delete_task():
                """Show the list of tasks, ask which one to delete, and remove it."""
                if not tasks:
                    print("Your to-do list is empty. Nothing to delete.")
                    return
                view_tasks()
                try:
                    task_number = int(input("Enter task number to delete:"))
                except ValueError:
                    print("Error: Please enter a valid integer.")
                    return
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f'Task "{removed_task}" has been removed.')
                else:
                    print("Error: Invalid task number. No task was deleted.")
                    return
                removed_task= tasks.pop(task_number - 1)
                print(f'Task "{removed_task}" has been removed.')
                def show_menu():
                    """Display the menu and prompt the user for a choice."""
                    print("\n============================")
                    print("     TO-DO LIST MENU")
                    print("============================")
                    print("1. Add task")
                    print("2. View tasks")
                    print("3. Delete task")
                    print("4. Quit")
                    choice = input("Enter your choice (1-4):").strip()
                    return choice

                def main():
                    """Main loop to run the to-do list application."""
                    while True:
                        choice = show_menu()
                        if choice == "1":
                            add_task()
                        elif choice == "2":
                            view_tasks()
                        elif choice == "3":
                            delete_task()
                        elif choice == "4":
                            print("Goodbye!")
                            break
                        else:
                            print("Error: Invalid choice. Please enter a number between 1 and 4.")
                            if __name__ == "__main__":
                                main()

