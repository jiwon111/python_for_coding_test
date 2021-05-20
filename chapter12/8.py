s = input()
string=[]
integer = []
for i in s:
    if i.isalpha():
        string.append(i)
    else:
       integer.append(int(i))
string.sort()
result = sum(integer)
for i in string:
    print(i, end='')
print(result)