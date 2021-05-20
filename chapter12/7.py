n = int(input())
num = []
i=0
sum1 = 0
sum2 = 0
while 1:
    if n/10==0:
        break
    num.append(n%10)
    i+=1
    n=n//10

mid = len(num)//2#3
for i in range(mid):
    sum1+=num[i]
for i in range(mid, len(num)):
    sum2+=num[i]
print(sum1)
print(sum2)
if sum1==sum2:
    print("LUCKEY")
else:
    print("READY")