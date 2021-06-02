def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent()