n, m = map(int, input().split())
data = []
tmp = [[0]*m for _ in range(n)]#벽을 설치한 뒤의 맵

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx < n and ny>=0 and ny<m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2#해당 위치에 바이러스 퍼짐, 다시 재귀
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score+=1
    return score

#dfs을 이용해 벽 설치하면서 안전 영역의 크기 계산
def dfs(cnt):
    global result

    #벽이 3개 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        #각 바이러스의 위치에서 전파
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        #안전 영역의 최댓값
        result = max(result, get_score())
        return

    #빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt+=1
                dfs(cnt)
                data[i][j] = 0
                cnt-=1

dfs(0)
print(result)