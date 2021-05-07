n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)#19

result = 0
while (start<=end):
    total = 0
    mid = (start+end)//2#9
    for x in array:
        if x>mid:
            total=total+x-mid
    if total<m:
            end = mid-1
    else:
            result=mid
            start=mid+1
print(result)