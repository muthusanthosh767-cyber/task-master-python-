import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found! Your list is empty.\n")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for idx, item in enumerate(tasks, 1):
        status = "Done" if item["done"] else "Pending"
        print(f"{idx}. [{status}] {item['task']}")
    print("------------------------\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task description: ").strip()
            if title:
                tasks.append({"task": title, "done": False})
                save_tasks(tasks)
                print("Task added successfully!\n")
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "4":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed['task']}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "5":
            print("Exiting TaskMaster. Have a productive day!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.\n")

if __name__ == "__main__":
    main()
          
