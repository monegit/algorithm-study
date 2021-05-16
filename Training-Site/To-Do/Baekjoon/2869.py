input = list(map(int, input().split()))

day, run = 0, 0

while True:
    day += 1
    run +=input[0]
    if run >= input[2]:
        break
    run-=input[1]

print(day)