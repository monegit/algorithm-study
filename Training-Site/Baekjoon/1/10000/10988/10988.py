letter = list(input())

result = 1

for i in range(int(len(letter) / 2)):
    if letter[i] != letter[-(i+1)]:
        result = 0
        break

print(result)