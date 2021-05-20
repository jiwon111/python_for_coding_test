n = int(input())
coin = list(map(int, input().split()))
result = 1
coin.sort()
#1 1 2 3 9
print(coin)
for x in coin:
    if result < x:
        break
    result = result+x

print(result)