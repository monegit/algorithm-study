import math

basemoney = 1000
money = int(input())
coin = 0

basemoney -= money

if basemoney >= 500:
    coin+= math.floor(basemoney/500)
    basemoney-=500*math.floor(basemoney/500)

if basemoney >= 100:
    coin += math.floor(basemoney/100)
    basemoney-=100*math.floor(basemoney/100)

if basemoney >= 50:
    coin += math.floor(basemoney/50)
    basemoney-=50*math.floor(basemoney/50)

if basemoney >= 10:
    coin += math.floor(basemoney/10)
    basemoney-=10*math.floor(basemoney/10)

if basemoney >= 5:
    coin += math.floor(basemoney/5)
    basemoney-=5*math.floor(basemoney/5)

print(int(coin)+basemoney)