n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        #왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = array[i-1][j-1]
        #바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = array[i - 1][j]

        array[i][j] = array[i][j]+max(up_left, up)

print(max(array[n-1]))