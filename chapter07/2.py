n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
req = list(map(int, input().split()))

def binary_sort(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return None

for i in req:
    result = binary_sort(array, i, 0, n - 1)
    if result != None:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')