n = int(input())

ugly = [0]*n
ugly[0] = 1

next2, next3, next5 = 2, 3, 5
idx2= idx3= idx5 = 0

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        idx2+=1
        next2 = ugly[idx2]*2
    if ugly[i] == next3:
        idx3+=1
        next3 = ugly[idx3]*3
    if ugly[i] == next5:
        idx5+=1
        next5 = ugly[idx5]*5

print(ugly[n-1])