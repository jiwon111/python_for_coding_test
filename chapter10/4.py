from collections import deque
import copy

v = int(input())

indegree = [0]*(v+1)

graph = [[]for _ in range(v+1)]

#강의 시간
time = [0]*(v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)#알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:#진입차수 0인 것 큐에 삽입
            q.append(i)

    while q:#큐가 빌 때까지
        now = q.popleft()#원소 꺼내고
        for i in graph[now]:#그 원소랑 연결된 노드들의 진입차수에서 1 빼기
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()