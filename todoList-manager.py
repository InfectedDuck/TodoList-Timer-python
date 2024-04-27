import os
import threading
import time
import random
from plyer import notification

# Class representing a task
class Task:
    # Constructor to initialize task properties
    def __init__(self, name, days, hours, minutes, seconds, priority):
        self.name = name
        # Calculate total remaining time in seconds
        self.remaining_time = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
        self.completed = False
        self.priority = priority

    # Method to update remaining time for the task
    def update_time_left(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1

    # Method to get the remaining time in a human-readable format
    def time_left(self):
        if self.remaining_time <= 0:
            return "Time's up!"
        else:
            days_left = self.remaining_time // (24 * 3600)
            time_left = self.remaining_time % (24 * 3600)
            hours_left = time_left // 3600
            time_left %= 3600
            minutes_left = time_left // 60
            time_left %= 60
            seconds_left = time_left
            return f"{int(days_left)} days, {int(hours_left)} hours, {int(minutes_left)} minutes, {int(seconds_left)} seconds"

# Function to display tasks in the to-do list
def display_tasks(tasks):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name} - Priority: {task.priority} - Time left: {task.time_left()}", end="\n")

# Function to continuously update task time
def update_task_time(tasks):
    while True:
        time.sleep(1)
        for task in tasks:
            task.update_time_left()
            # Send notification if 60 seconds left
            if task.remaining_time == 60:
                notification_title = f"{task.name} - 60 Seconds Left!"
                notification_text = f"{task.name} have 60 seconds to finish."
                notification.notify(title=notification_title, message=notification_text)
            # Send notification when time is up
            if task.remaining_time == 0:
                notification_title = f"{task.name} - Time's up"
                notification_text = f"{task.name} have to be completed!"
                notification.notify(title=notification_title, message=notification_text)

# Function to add a task to the to-do list
def add_task(tasks):
    task_name = input("Enter task name: ")
    days = int(input("Enter days: "))
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    priority = input("Enter priority (low, medium, high): ")
    new_task = Task(task_name, days, hours, minutes, seconds, priority)
    tasks.append(new_task)
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(tasks, completed_tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    print("Your tasks are:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name}")
    try:
        task_index = int(input("Enter the index of the task you want to complete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task index.")
            return
        task_to_remove = tasks[task_index]
        confirmation = input(f"Did you really complete this task?'{task_to_remove.name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            tasks.remove(task_to_remove)
            completed_tasks.append(task_to_remove)
            print("Task successfully completed")
        else:
            print("Task completion canceled.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Function to update an existing task
def update_task(tasks):
    if not tasks:
        print("No tasks to update.")
        return
    print("Your tasks are:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name}")
    try:
        task_index = int(input("Enter the index of the task you want to update: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task index.")
            return
        new_name = input("Enter the new name for the task: ")
        days = int(input("Enter new days: "))
        hours = int(input("Enter new hours: "))
        minutes = int(input("Enter new minutes: "))
        seconds = int(input("Enter new seconds: "))
        priority = input("Enter new priority (low, medium, high): ")
        tasks[task_index].name = new_name
        tasks[task_index].remaining_time = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
        tasks[task_index].priority = priority
        print("Task updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid index and time.")

# Function to sort tasks based on user-specified criteria
def sort_tasks(tasks):
    sort_option = input("Choose sorting option (time/name/priority): ")
    if sort_option.lower() == "time":
        tasks.sort(key=lambda task: task.remaining_time)
    elif sort_option.lower() == "name":
        tasks.sort(key=lambda task: task.name)
    elif sort_option.lower() == "priority":
        tasks.sort(key=lambda task: task.priority)
    else:
        print("Invalid sorting option.")

# Function to display completed tasks
def show_completed_tasks(completed_tasks):
    print("Completed tasks:", [task.name for task in completed_tasks])

# Main function to run the program
def main():
    motivational_sentences = [
        "Great job! You're making progress!",
        "One step closer to your goals!",
        "Keep up the amazing work!",
        "You're on fire! Keep going!",
        "Each task completed is a victory!",
        "Success is built one task at a time!",
        "You're unstoppable!",
        "Well done! Your hard work pays off!",
        "Every task completed brings you closer to success!",
        "You're turning dreams into reality!",
        "Your dedication shines through!",
        "Another task conquered! You're unstoppable!",
        "You're making it happen!",
        "Persistence pays off! Keep it up!",
        "You're making progress every day!",
        "Another task checked off the list!",
        "You're a productivity powerhouse!",
        "Success is just a series of completed tasks!",
        "You're making your dreams a reality, one task at a time!",
        "You're getting closer to your goals with every task!",
        "Your commitment is inspiring!",
        "You're turning your vision into reality!",
        "Celebrate each task completed!",
        "Your determination is unmatched!",
        "You're a task-completing machine!",
        "One more task down, countless more to go!",
        "Each task completed is a step forward!",
        "Your productivity game is strong!",
        "You're crushing it!",
        "Your persistence is paying off!",
        "Keep up the fantastic work!",
        "You're making waves with your productivity!",
        "Success is in the details, and you're nailing it!",
        "Every task completed is a victory lap!",
        "Your focus and determination are paying dividends!",
        "You're unstoppable when you set your mind to it!",
        "Keep pushing forward! You're doing great!",
        "You're proving that nothing can stand in your way!",
        "Every completed task brings you closer to your dreams!",
        "You're a task-master! Keep conquering!"
    ]
    tasks = []  # Initialize empty list to store tasks
    completed_tasks = []  # Initialize empty list to store completed tasks
    # Create and start a thread to update task time continuously
    task_time_updater = threading.Thread(target=update_task_time, args=(tasks,))
    task_time_updater.daemon = True  # Daemonize the thread so it terminates with the main program
    task_time_updater.start()  # Start the thread
    while True:  # Infinite loop for user interaction
        display_tasks(tasks)  # Display tasks in the to-do list
        print("\nOptions:")
        # Print available options
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Sort Todo List")
        print("4. Show Completed Tasks")
        print("5. Show Incomplete Tasks")
        print("6. Update Task")
        print("7. Exit and Delete All Tasks")
        option = input("Enter your option: ")  # Input user option
        if option == "1":  # If option is to add a task
            add_task(tasks)  # Call function to add a task
        elif option == "2":  # If option is to complete a task
            complete_task(tasks, completed_tasks)  # Call function to complete a task
        elif option == "3":  # If option is to sort tasks
            sort_tasks(tasks)  # Call function to sort tasks
        elif option == "4":  # If option is to show completed tasks
            show_completed_tasks(completed_tasks)  # Call function to show completed tasks
        elif option == "5":  # If option is to show incomplete tasks
            display_tasks(tasks)  # Display incomplete tasks
        elif option == "6":  # If option is to update a task
            update_task(tasks)  # Call function to update a task
        elif option == "7":  # If option is to exit
            print("Exiting the program. To run the program again, please execute it again.")  # Print exit message
            break  # Exit the loop and program
        else:  # If invalid option
            print("Invalid option")  # Print message

if __name__ == "__main__":
    main()  # Call the main function to start the program
