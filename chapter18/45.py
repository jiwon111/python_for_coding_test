from collections import deque

for _ in range(int(input())):
    n = int(input())#노드 갯수

    indegree = [0]*(n+1)
    graph = [[False]*(n+1) for i in range(n+1)]

    data = list(map(int, input().split()))#작년 순위
    #간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())

        #간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] +=1
            indegree[b] -=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a]-=1
            indegree[b]+=1

    #topological
    result =[]
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True#위상 정렬 결과가 오직 하나인지 여부
    cycle = False#사이클이 존재하는지

    #노드의 갯수만큼 반복
    for i in range(n):
        #큐가 비어있으면 사이클이 있다는 의미
        if len(q) == 0:
            cycle = True
            break
        #2개 이상이면 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)

        #해당 노드와 연결된 노드들의 진입차수에서 1빼기
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()