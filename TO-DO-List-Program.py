# TO - DO List 
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'status': 'not done'})

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
        else:
            print("Invalid task index")

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['status'] = 'done'
        else:
            print("Invalid task index")

    def view_tasks(self):
        if not self.tasks:
            print("There are no tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task['task']} - {task['status']}")

def main():
    todoList = TodoList()

    while True:
        print("To-Do List Application\n")
        print("1. Add the Task")
        print("2. Update the Task")
        print("3. Mark the Task as Done")
        print("4. View the Tasks")
        print("5. Exit")

        choice = input("Enter your choice which you want to do : ")

        if choice == '1':
            task = input("Enter the task: ")
            todoList.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            todoList.update_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter the task index to mark as done: "))
            todoList.mark_task_as_done(index)
        elif choice == '4':
            todoList.view_tasks()
        elif choice == '5':
            break
        else:
            print("Your input is not a valid choice, please try again.")

if __name__ == "__main__":
    main()
