def bfs(queue, v):
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.pop(0)
        print(v)

        for w in G[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True

G = [[],
    [2, 3],
    [4, 5],
    [7],
    [6],
    [6],
    [7],
    []]

queue = []
visited = [False]*(len(G)+1)

bfs(queue, 1)