from collections import deque

n, k = map(int, input().split())
graph = []#전체 보드 정보
data = []#바이러스에 대한 정보

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j]!=0:
            #(바이러스 종류, 시간, 위치x, 위치y) 삽입
            data.append((graph[i][j], 0, i, j))
data.sort()#낮은 번호의 바이러스가 먼저 증식하기 때문에
input_s, input_x, input_y = map(int, input().split())
q = deque(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#bfs
while q:
    virus, s, x, y = q.popleft()

    if s == input_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #해당 위치로 이동할 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<n:
            #아직 방문하지 않은 위치라면 바이러스 삽입
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[input_x - 1][input_y - 1])

