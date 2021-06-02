def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] =a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*(n+1)
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()#간선을 비용순으로 정렬
total = 0 #전체 가로등 비용

for edge in edges:
    cost, a, b = edge
    total+=cost

    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost

print(total-result)