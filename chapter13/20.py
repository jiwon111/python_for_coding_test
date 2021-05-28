from itertools import combinations

n = int(input())
board = []#복도
teachers = []#선생님 위치
spaces = []#빈 공간 위치

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

#특정 방향으로 감시 진행
def watch(x, y, direction):
    #왼쪽으로
    if direction == 0:
        while y>=0:
            if board[x][y] == 'S':#학생이 있는 경우
                return True
            if board[x][y] == 'O':#장애물 있는 경우
                return False
            y-=1

    #오른쪽으로
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':#학생이 있는 경우
                return True
            if board[x][y] == 'O':#장애물이 있는 경우
                return False
            y+=1

    #위쪽으로
    if direction == 2:
        while x>=0:
            if board[x][y] == 'S':#학생이 있는 경우
                return True
            if board[x][y] == 'O':#장애물이 있는 경우
                return False
            x-=1

    #아래쪽으로
    if direction == 3:
        while x<n:
            if board[x][y] == 'S':#학생이 있는 경우
                return True
            if board[x][y] == 'O':#장애물이 있는 경우
                return False
            x+=1


def process():
    #모든 선생님의 위치를 확인
    for x, y in teachers:
        for i in range(4):#4가지 방향으로 감시
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):#빈 공간에서 3개를 뽑는 조합을 모두 확인
    for x, y in data:#장애물 설치해보기
        board[x][y]='O'
    if not process():
        find = True
        break
    for x, y in data:#장애물 다시 삭제
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")
