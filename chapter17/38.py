n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

#간선에 대한 정보를 입력받아 초기화
for _ in range(m):
    #x에서 y로 가는 비용을 1로 초기화
    x, y = map(int, input().split())
    graph[x][y] = 1

#플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0

#각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크함
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:#모든 노드에 대해 도달 가능한지 체크
            cnt+=1
    if cnt == n:#특정한 노드의 카운트 값이 n이라면 해당 노드의 정확한 순위를 알 수 있다는 것을 의미
        result += 1

print(result)