# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%H:%M, %d-%b-%Y")
print("It is:", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1}-{todo.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")

            print(f"You changed '{todos[number - 1].strip()}' with '{new_todo.strip()}'.")
            todos[number - 1] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your 'edit' command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])
            todos = functions.get_todos()
            completed_todo = todos[number - 1]
            todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"Todo {completed_todo.strip().capitalize()} was completed.")

        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown command :)")

print("Bye!")
