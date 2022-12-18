
def myFunc(string, index, char):
    string = string[ :index] + char + string[index+1: ] # char = string[index]
    return string

def main():
    userString = input()
    index, char = input().split()
    result = myFunc(userString, int(index), char)
    print(result)
main()                          #start running the code
