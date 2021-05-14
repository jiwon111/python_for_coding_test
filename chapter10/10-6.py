from collections import deque

#노드의 갯수, 간선의 갯수
v, e = map(int, input().split())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]

#간선 정보 입력받고 진입차수 설정
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = []#결과
    q = deque()

#진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:#큐가 빌 때까지 반복
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i]-=1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()