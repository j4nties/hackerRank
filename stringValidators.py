str = input()
isAlnum, isAlpha, isDigit, isLower, isUpper = False, False, False, False, False

for char in str:
    if char.isalnum():
        isAlnum = True
    if char.isalpha():
        isAlpha = True
    if char.isdigit():
        isDigit = True
    if char.islower():
        isLower = True
    if char.isupper():
        isUpper = True


print(isAlnum, isAlpha, isDigit, isLower, isUpper, sep = "\n")

