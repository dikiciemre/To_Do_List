# The array to which tasks will be added has been defined
tasks = []


# Add function
def add_task(task):
    tasks.append(task)
    print(f"'{task}' Has Been Added.")


# List function for listing tasks
def list_tasks():
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# delete function
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"'{removed_task}' Has Been Deleted .")
    else:
        print("Invalid Entry. Please Try Again")



while True:
    print("\nPlease Select An Action You Want :")
    print("1. Add New Task")
    print("2. List Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter Your Choice (1/2/3/4): ")

    if choice == '1':
        new_task = input("Enter Your New Task: ")
        add_task(new_task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        task_index = int(input("please select the value you want to delete : "))
        remove_task(task_index)
    elif choice == '4':
        print("Exiting The To Do List Programme")
        break
    else:
        print("Invalid Entry. Please Try Again.")
