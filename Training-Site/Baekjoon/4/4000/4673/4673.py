self_number = [0] * (10000 + 100)

for i in range(len(self_number) - 100):
    result = 0
    value = self_number[i]
    for j in range(len(list(str(i)))):
        result = result + int(list(str(i))[j])
    result = result + i
    self_number[result] = self_number[result] + 1

for i in range(len(self_number) - 100):
    if self_number[i] <= 0:
        print(i)