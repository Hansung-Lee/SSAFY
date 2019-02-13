N = 7 # 노드의 개수
edge = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]] # 간선


tree = [[] for x in range(N)]
visited = [False for x in range(N)]

for e in edge:
    tree[e[0]-1].append(e[1]-1)
    tree[e[1]-1].append(e[0]-1)

stack = []

def dfs(v):
    stack.append(v)

    while stack:
        node_v = stack.pop()

        if visited[node_v]:
            continue
        
        print(node_v+1)
        visited[node_v] = True
        stack.extend(tree[node_v][::-1])

dfs(0)