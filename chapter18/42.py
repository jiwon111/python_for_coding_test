G = int(input())
P = int(input())

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*(G+1)

for i in range(1, G+1):
    parent[i] = i

result = 0
for i in range(P):
    plane = find_parent(parent, int(input()))
    if plane == 0:
        break
    union_parent(parent, plane, plane-1)
    result += 1

print(result)