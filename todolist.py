todolist = []

while True:
    # The menu
    print("---------")
    print("To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Completed")
    print("4. Remove Task")
    print("5. Quit Program")
    print("6.Clear the whole schedule")
    choice = input("Enter Your choice: ")

    if choice == "1":
        # Add to the to-do list
        task = input("Enter a task to the schedule: ")
        todolist.append({"task": task, "completed": False})
        print("Task added!")

    elif choice == "2":
        # View all tasks
        print("\nTo-Do List:")
        for index, item in enumerate(todolist, start=1):
            status = "✓" if item["completed"] else ""
            print(f"{index}. [{status}] {item['task']}")

    elif choice == "3":
        # Mark a task as completed
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(todolist):
            todolist[task_index]["completed"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")

    elif choice == "4":
        # Remove a task
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(todolist):
            removed_task = todolist.pop(task_index)
            print(f"{removed_task['task']} is now removed")
        else:
            print("Invalid task number")

    elif choice == "5":
        # Quit
        print("Goodbye!")
        break
    elif choice == "6":
        #Clear the whole thing
        confirm = input("This will clear the whole schedule are you sure?(yes/no):").lower()
        if confirm == "yes":
           todolist.clear()
           print("List Cleared!")
        else:
            print("List not cleared!")
        
    
    else:
        print("Invalid choice")
