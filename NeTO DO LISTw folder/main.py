# To-Do List Application
# Author: Nitin Gupta

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

tasks = []

def view_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{i}. {task['name']} [{status}]")

def add_task():
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False})
    print("✅ Task added successfully!")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        tasks.pop(index)
        print("🗑️ Task removed successfully!")
    except (ValueError, IndexError):
        print("⚠️ Invalid input!")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[index]["completed"] = True
        print("🎉 Task marked as completed!")
    except (ValueError, IndexError):
        print("⚠️ Invalid input!")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.")
