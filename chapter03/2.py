n, m, k = map(int, input().split())
#n개의 data, m번 더해서 가장 큰 수, k번 초과하여 중복할 수 없음
data = list(map(int, input().split()))
result = 0
data.sort()

max1 = data[n-1]
max2 = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

#가장 큰 수 더하기
result+=count*max1
#두 번째로 큰 수 더하기
result+=(m-count)*max2

print(result)