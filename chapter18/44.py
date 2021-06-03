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

n = int(input())
parent = [0]*(n+1)
edges = []
result = 0
for i in range(1, n+1):
    parent[i] = i

x=[]
y=[]
z=[]
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()#간선 정렬

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):#사이클이 발생하지 않는 경우
        union_parent(parent, a, b)#최소 신장 트리에 포함
        result+=cost

print(result)