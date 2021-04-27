data = input()
row = int(data[1])
col = int(ord(data[0]))-int(ord('a')) + 1

step = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0

for i in step:
    next_row = row+i[0]
    next_col = col+i[1]
    if next_row >=1 and next_row<=8 and next_col>=1 and next_col<=8:
        cnt+=1
print(cnt)