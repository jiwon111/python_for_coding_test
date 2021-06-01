INF = int(1e9)
n = int(input())
m = int(input())
graph= [[INF]*(n+1)for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:#자신한테 가는 비용은 0으로 초기화
            graph[a][b] = 0

#간선 정보 입력받음
for i in range(m):
    a, b, c = map(int, input().split())

    #가장 짧은 간선만 저장
    if c<graph[a][b]:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()