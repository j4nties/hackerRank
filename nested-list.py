students = []
grades = []
result = []
studentAmount = int(input())

for _ in range(studentAmount):
    name = input()
    score = float(input())
    students.append([name, score])
    grades.append(score)

grades = list(set(grades))#list => set => list convertion. no repetation del same grades 
grades = sorted(grades, key= float)#sorting grades

##========================List Comprehensions
[result.append(student[0]) for student in students if grades[1] == student[1] ]
#?   do this      /         loop        /           condition

result = sorted(result)#Sorting Names Alphabetically and printing result!

[print(name) for name in result]
