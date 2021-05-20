n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()
cnt = 0

print(ball)
#1 2 2 3 3
for i in range(len(ball) - 1):
    for j in range(i+1, len(ball)):
        if ball[i] == ball[j]:
            continue
        cnt+=1
        print("(%d번, %d번)"%(i+1, j+1))

print(cnt)