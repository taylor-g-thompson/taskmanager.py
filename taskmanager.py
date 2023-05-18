import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        completed INTEGER
    )
    """
)
conn.commit()

def add_task():
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")

    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)",
        (title, description),
    )
    conn.commit()
    print("Task added successfully!")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            task_id, title, description, completed = task
            status = "Completed" if completed else "Not completed"
            print(f"Task ID: {task_id}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Status: {status}")
            print("-" * 20)

def mark_task_as_completed():
    task_id = input("Enter the ID of the task to mark as completed: ")

    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print("Task marked as completed!")

def delete_task():
    task_id = input("Enter the ID of the task to delete: ")

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted!")

def menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_as_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()

# Close the database connection
conn.close()
