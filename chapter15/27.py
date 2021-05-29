n, x = map(int, input().split())
data = list(map(int, input().split()))

def count_by_value(array, x):#몇 개인지 카운트
    length = len(array)

    a = first(array, x, 0, n-1)#x가 처음 등장한 인덱스

    if a == None:
        return 0

    b = last(array, x, 0, n-1)#x가 마지막으로 등장한 인덱스

    return b-a+1

def first(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2

    #해당 값을 가진 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target>array[mid-1]) and array[mid] == target:
        return mid
    #mid보다 target이 작거나 같은 경우 왼쪽 확인
    elif array[mid]>=target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

#마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2

    if (mid == n-1 or target<array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid]>target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)

cnt = count_by_value(data, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)