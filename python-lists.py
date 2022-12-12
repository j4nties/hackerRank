#bad solution
N = int(input())
myList = []
def inserter(lst):
    lst = [int(i) for i in lst]
    myList.insert(lst[0], lst[1])
def remover(numb):
    numb = int(numb)
    myList.remove(numb)

for _ in range(N):
    userInput = input()
    userInput = userInput.strip().split()
    if userInput[0] == 'insert':
        inserter(userInput[1:])
    elif userInput[0] == 'print':
        print(myList)
    elif userInput[0] == 'remove':
        remover(userInput[1])
    elif userInput[0] == 'append':
        myList.append(int(userInput[1]))
    elif userInput[0] == 'sort':
        myList = sorted(myList)
    elif userInput[0] == 'pop':
        myList.pop()
    elif userInput[0] == 'reverse':
        myList = myList[::-1] 