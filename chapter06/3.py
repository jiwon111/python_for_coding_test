n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda student: student[1])#점수를 기준으로 정렬

for student in array:
    print(student[0], end=' ')