def pow(a,b,m=1):
    return [a**b,a**b%m]

a, b, m = int(input()),int(input()),int(input())
results = pow(a,b,m)
for result in results:
    print(result)