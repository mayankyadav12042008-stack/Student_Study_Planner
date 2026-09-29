
from tasks import tasks

def show_schedule():
    if not tasks:
        print("No scheduled tasks yet.")
        return

    print("\n--- STUDY SCHEDULE ---")
    for task in sorted(tasks, key=lambda t: t["deadline"]):
        print(f"{task['deadline']} - {task['subject']}: "
              f"{task['title']}")
