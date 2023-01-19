def divmod(a,b):
    a2 = int(a / b)
    b = int(a % b)
    return a2,b

a= int(input())
b= int(input())
res = (divmod(a,b))
print(*res,res, sep = "\n")

