a = input()
b = input()

n = len(a)
m = len(b)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j

#최소 편집 거리 계산
for i in range(1, n+1):
    for j in range(1, m+1):
        #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:#삽입, 삭제, 교체 중에서 최소 비용을 찾아 대입
            dp[i][j] = 1+min(dp[i][j - 1], dp[i-1][j], dp[i-1][j-1])

print(dp[n][m])