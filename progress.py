
from tasks import tasks

def show_progress():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    print("\n--- STUDY PROGRESS ---")
    print("Total tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)

    if total > 0:
        percentage = (completed / total) * 100
        print(f"Completion: {percentage:.1f}%")
    else:
        print("Completion: 0%")