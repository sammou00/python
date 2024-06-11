class TodoList:
    def __init__(self):
        self.todo_list = []

    def get_list(self):
        return self.todo_list
    
    def get_todo_by_id(self, id):
        for todo in self.todo_list:
            if todo.get_id() == id:
                return todo
        return None
    
    def get_count(self):
        return len(self.todo_list)
    
    def add(self, todo):
        self.todo_list.append(todo)

    def update(self, todo):
        for i in range(len(self.todo_list)):
            if self.todo_list[i].get_id() == todo.get_id():
                self.todo_list[i] = todo
                break

    def remove(self, todo):
        self.todo_list.remove(todo)

    def clear(self):
        self.todo_list.clear()

    def __str__(self):
        return str([todo.get_title() for todo in self.todo_list])

class Todo:
    last_id = 0

    def __init__(self, title):
        Todo.last_id += 1
        self.id = Todo.last_id
        self.title = title
    
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

def main():
    todo_list = TodoList()

    while True:
        print("-----------------------------")
        print("Welcome to the Todo List App")
        print("-----------------------------")
        print("1. Get list\n2. Get todo by id\n3. Get count\n4. Add todo\n5. Update todo\n6. Remove todo\n7. Clear all todos\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(todo_list.get_list())
        elif choice == '2':
            id = int(input("Enter the id of the todo: "))
            todo = todo_list.get_todo_by_id(id)
            if todo:
                print(todo.get_title())
            else:
                print("Todo not found.")
        elif choice == '3':
            print(todo_list.get_count())
        elif choice == '4':
            title = input("Enter the title of the todo: ")
            todo = Todo(title)
            todo_list.add(todo)
        elif choice == '5':
            id = int(input("Enter the id of the todo: "))
            title = input("Enter the new title of the todo: ")
            todo = Todo(title)
            todo_list.update(todo)
        elif choice == '6':
            id = int(input("Enter the id of the todo: "))
            todo = todo_list.get_todo_by_id(id)
            if todo:
                todo_list.remove(todo)
                print("Todo removed successfully.")
            else:
                print("Todo not found.")
        elif choice == '7':
            todo_list.clear()
            print("All todos cleared.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
