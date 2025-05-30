from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_prompt = input("Type add, show, edit, complete or exit:")
    user_action = user_prompt.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos=get_todos()
        todos.append(todo + "\n")
        write_todos(todos)
    elif user_action.startswith("show"):
        todos=get_todos()
        for i,item in enumerate(todos):
            item=item.strip('\n')
            print(f"{i+1}-{item}")
    elif user_action.startswith("edit"):
        try:
            sn=int(user_action[5:])
            sn= sn-1
            todos=get_todos()

            new_todo=input("Enter new To-do:")
            todos[sn]=new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Command is not valid.")
            continue
        except IndexError:
            print("There is no todo with this index")
            continue
    elif user_action.startswith("complete"):
        try:
            i= int(user_action[9:])
            todos=get_todos()
            todo_to_remove=todos[i-1].strip("\n")
            todos.pop(i-1)
            write_todos(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except ValueError:
            print("Command is not valid.")
            continue
        except IndexError:
            print("There is no todo with this index")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye")