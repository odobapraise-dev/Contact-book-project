tasks = []

while True:
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input('Enter a new task: ')
        tasks.append(task)
        print(f"Task '{task}' added ")

    elif choice == '2':
        if not tasks:
            print('no task yet')
        else:
            print(tasks)
        
    

    elif choice == '3':
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed ")
        else:
            print("Task not found!")

    elif choice == '4':
        
        break

    else:
        print("Invalid choice, try again!")
