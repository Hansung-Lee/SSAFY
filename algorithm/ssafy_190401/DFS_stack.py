def dfs(stack, v):
    stack.append(v)
	visited[v] = True

    while stack:
        v = stack.pop()
        print(v)

		for w in G[v]:
			if not visited[w]:
				stack.append(w)
				visited[w] = True

G = [[1],
    [2],
    [3, 4],
    [],
    []]

stack = []
visited = [False]*len(G)

dfs(stack, 0)