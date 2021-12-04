money = int(input())/1000

first = (money*22)*10
second = (money*80)*10

print(int((money * 1000) - first), int(money*1000-(((money*1000-second)*22)/100)))
