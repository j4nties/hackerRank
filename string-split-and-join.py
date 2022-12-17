
def split_and_join(string):
    string = string.strip()     #removing whitespaces
    words = string.split(" ")   # string to list  #list of string word by word
    return "-".join(words)      # list to string  # adding - between each words and getting a string

def main():
    myString = input()
    result = split_and_join(myString)
    print(result)

main()                          #start running the code
