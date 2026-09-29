
from tasks import add_task, view_tasks, complete_task, delete_task
from schedule import show_schedule
from progress import show_progress

def main():
    while True:
        print("\n===== STUDENT STUDY PLANNER =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. View schedule")
        print("6. View progress")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_schedule()
        elif choice == "6":
            show_progress()
        elif choice == "7":
            print("Thank you for using Study Planner!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()