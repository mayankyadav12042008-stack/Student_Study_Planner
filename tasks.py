
tasks = []

def add_task():
    subject = input("Enter subject: ")
    title = input("Enter task: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")

    if not subject.strip() or not title.strip() or not deadline.strip():
        print("All fields are required.")
        return

    task = {
        "subject": subject,
        "title": title,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} | {task['subject']} | "
              f"{task['deadline']} | {status}")

def complete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")