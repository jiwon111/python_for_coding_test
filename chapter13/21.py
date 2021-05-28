from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 경신
def process(x, y, index):
    united = []#(x, y)와 연합된 나라 정보
    united.append((x, y))

    #BFS
    q = deque()
    q.append((x, y))
    union[x][y] = index#현재 연합의 번호 할당
    summary = graph[x][y]#현재 연합의 전체 인구 수
    cnt = 1#현재 연합의 국가 수

    while q:
        x, y = q.popleft()

        #4가지 방향을 확인하며
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #바로 옆에 있는 나라를 확인하여
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l<=abs(graph[nx][ny] - graph[x][y])<=r:
                    q.append((nx, ny))
                    #연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    cnt+=1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary//cnt
    return cnt

total_cnt = 0

#더 이상 인구 이동을 할 수 없을 때까지 반복
while 1:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:#아직 해당 나라가 처리되지 않았다면
                process(i, j, index)
                index+=1

    if index == n*n:
        break
    total_cnt += 1

print(total_cnt)