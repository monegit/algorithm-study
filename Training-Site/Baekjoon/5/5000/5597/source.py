student = []

for i in range(30):
    student.append(i+1)

for _ in range(28):
    student.remove(int(input()))

for i in range(len(student)):
    print(student[i])
