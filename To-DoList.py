tasks = []
def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}:{task}")
    else:
        print("Your list is empty")
def welcome():
    while True:
        try:
            task_option = int(input("welcome to the To-Do List App!\nMenu: \n1. Add a task \n2. View tasks \n3. Mark a task as complete \n4. Delete a task \n5. quit\n Please select an option: "))
            if task_option == 1:
                addtask()
            elif task_option == 2:
                viewtask()
            elif task_option == 3:
                marktask()
            elif task_option == 4:
                deletetask()
            elif task_option == 5:
                print("Have a good day. Thanks for using the To-Do List App")
                break
            else:
                print("please enter a valid number 1-5")
        except ValueError:
            print("Please enter a valid number 1-5")

def addtask():
        while True:
            add = input("What would you like to add to your To-Do List? \n Enter 5 to go back to the menu:\n")
            if add == "5":
                break
            tasks.append(add)
            

def viewtask():
    display_tasks()
    try:
        next_action = int(input("press 1 to return to the menu, press 2 to quit: "))
        if next_action == 1:
            return
        elif next_action == 2:
            print("bye")
            exit()
    except ValueError:
        print("Please enter a correct value")  

def marktask():
    if tasks:
        display_tasks()
        try:
            completed_task = int(input("What would you like to mark as completed? "))
            if 1 <= completed_task <= len(tasks):
                done_task = tasks.pop(completed_task-1)
                print(f"task {done_task} completed")
            else:
                print("invalid number please select a number from the list")
        except ValueError:
            print("No characters, please enter a valid number")
    else:
        print("your list is empty! Take a day off will ya?")
    try:
        home_or_done = int(input("Do you want to (1) go back to the menu, (2) mark more task complete: "))
        if home_or_done == 1:
            return
        elif home_or_done == 2:
            marktask()        
    except ValueError:
        print("Please make a choice between 1-3")

def deletetask():
    if tasks:
        display_tasks()
        try:
            remove_task=int(input(f"Which task would you like to delete: "))
            if 1 <= remove_task <= len(tasks):
                deleted_task = tasks.pop(remove_task - 1)
                print(f"{deleted_task} deleted.")
            else:
                print("please select a valid number")
        except ValueError:
            print("please make a valid selection.")
    else:
        print("your list is empty")
                
welcome()
