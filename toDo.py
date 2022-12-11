import time, os
todos = []

def display():
    userInput = input("1)add\n2)show\n3)edit\n4)delete\n5)exit\n-> ")
    return userInput

while(True):
    menuInput = display()
    menuInput = menuInput.strip()
    ## '1 ' if input includes whitespace'es '1' != '1  ' .strip()
    match menuInput:
        case '1':#add
            todo = input("Enter a todo: ")
            todo = todo.title()
            ##title makes uppercase first letters
            todos.append(todo)
        case '2':#show
            #?todos is a list of string
            os.system("cls")
            for task in todos:
                print(task)
        case '3':#edit
            if todos != []:
                index = int(input("Enter a number of it: "))
                todos[index-1] = input("Change with that =>  ").title()
            else:
                print("There is no task to change!")
        case '4':#delete
            index = int(input("Enter a number of it: "))
            todos.pop(index-1)
        case '5':#exit
            break
        case _:
            print("Wrong input!")
    time.sleep(0.8)
    os.system("cls")
    time.sleep(0.2)
print("Bye!")