#  THIS PROJECT IS DONE BY VINAY DIWATE
import datetime

def greet_user():
    """Greets the user with a personalized message based on the time of day."""
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        print("Good morning! Ready to tackle your tasks today?")
    elif 12 <= current_hour < 18:
        print("Good afternoon! How's your day going so far?")
    else:
        print("Good evening! Time to wind down and reflect on your progress.")

def display_tasks(task_list):
    """Displays the to-do list in a clear and organized format."""
    print("\nHere's your current to-do list:\n")
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task}")

def add_task():
    """Adds a new task to the list, providing helpful prompts and feedback."""
    new_task = input("What would you like to add to your to-do list? ")
    task_list.append(new_task)
    print(f"Got it! I've added '{new_task}' to your list.")

def mark_task_complete():
    """Marks a task as complete, celebrating the user's progress."""
    task_number = int(input("Which task would you like to mark as complete? (Enter the number) "))
    completed_task = task_list.pop(task_number - 1)
    print(f"Congratulations! You've completed '{completed_task}'. Keep up the great work!")

task_list = []  # Initialize the to-do list

greet_user()

while True:
    print("\nWhat would you like to do?")
    choice = input("1. View tasks\n2. Add a task\n3. Mark a task complete\n4. Exit\n")

    if choice == "1":
        display_tasks(task_list)
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        print("See you next time! Have a productive day.")
        break
    else:
        print("Invalid choice. Please try again.")