from plyer import notification
from threading import Timer
from datetime import datetime, timedelta


def add_task(tasks,times):
    task = input("Enter a task: ")
    tasks.append(task)
    notif_time = input("Enter a time in the format %H:%M: ")
    times.append(notif_time)
    # for current time
    current_time = datetime.now().time()

    # Convert the user-defined time string to a datetime object
    user_time = datetime.strptime(notif_time, "%H:%M").time()

    # Calculate the time difference to use in reminder notification
    if current_time < user_time:
        difference = datetime.combine(datetime.today(), user_time) - datetime.combine(datetime.today(), current_time)
    else:
        # If the user-defined time is earlier or equal to the current time, assume it's for the next day
        difference = datetime.combine(datetime.today() + timedelta(days=1), user_time) - datetime.combine(datetime.today(), current_time)
    
    # Check if user wants input for the desired tasks
    if input("Want notification? If so please enter 'yes': ") == "yes":
        def reminder():
            notification.notify(title="Reminder", message=task, timeout=20)
        # Using timer function reminder is shown as notification
        timer = Timer(difference.total_seconds(), reminder)
        timer.start()
    
    print("Task added successfully!")
    
# display tasks function to show all the tasks displayed       
def display_tasks(tasks,times):
    if len(tasks) == 0:
        print("No tasks for the day.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# main function         
def main():
    tasks = []
    times = [] 
   
    while True:
        print("-------To-Do tasks for the day------")
        print("1. Add Tasks with time")
        print("2. Display Tasks")
        print("0. Exit the app")
        choice = input("Enter your choice (0-2): ")

        if choice == "1":
            add_task(tasks,times)
        elif choice == "2":
            display_tasks(tasks,times)
        elif choice == "0":
            break
        else:
            print("Please try again. ")

if __name__ == "__main__":
    main()
