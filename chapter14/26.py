'''import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0


while len(heap)!=1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum = one+two
    result += sum
    heapq.heappush(heap, sum)

print(result)'''

n = int(input())
card = []
for i in range(n):
    card.append(int(input()))
card.sort()
sum = card[0]
result = 0

for i in range(n-1):
    sum+=card[i+1]
    result+=sum

print(result)