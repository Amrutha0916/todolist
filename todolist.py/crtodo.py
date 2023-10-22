import json
import os

# Function to load tasks from a file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:       
        print("There are no tasks.")
    else:
        print("\nTodo List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

def add_task(tasks, new_task, priority, due_date):
    task = {
        'description': new_task,
        'priority': priority,
        'due_date': due_date
    }
    tasks.append(task)
    print(f"Task '{new_task}' added to the to-do list.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1) 
        print(f"Task '{removed_task['description']}' removed from the to-do list.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()
    
    while True: 
        print("\nSelect an option:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            priority = input("Enter the priority (high/medium/low): ")
            due_date = input("Enter the due date: ")
            add_task(tasks, new_task, priority, due_date)
            save_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting the todo list.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
      
            
            
              