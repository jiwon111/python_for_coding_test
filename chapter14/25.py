n = int(input())
stages = list(map(int, input().split()))

result = []
length = len(stages)
for i in range(1, n+1):
    cnt = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = cnt/length

    length-=cnt
    result.append((i, fail))

result = sorted(result, key=lambda t:t[1], reverse = True)
result = [i[0] for i in result]
print(result)