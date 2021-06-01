n = int(input())
array = list(map(int, input().split()))

array.reverse()
dp = [1]*n

#LIS
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))#열외시켜야 하는 병사의 최소 수