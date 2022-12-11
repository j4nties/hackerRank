n = int(input())
student_marks = {}
result = 0
for _ in range(n):
    name, *line = input().split() #line list of grades ['67', '68', '69']
    scores = list(map(float, line))# grades str to float convertion
    student_marks[name] = scores # dictionary student_marks[key] = value
query_name = input() # which key?
for grade in student_marks[query_name]:# take avarage of grades of the person
    result += grade/3
print(f"{result:.2f}")## 56.0 to 56.00 adding digit .0 .00

"""====Input====
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika 
"""
"""====Output====
    56.00 
"""