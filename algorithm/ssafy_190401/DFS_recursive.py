def dfs_Recursive(G, v):
    visited[v] = True
    print(v)

    for w in G[v]:
        if not visited[w]:
            dfs_Recursive(G, w)

G = [[1],
    [2],
    [3, 4],
    [],
    []]

visited = [False]*len(G)

dfs_Recursive(G, 0)