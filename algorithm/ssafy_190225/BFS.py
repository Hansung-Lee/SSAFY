input_text = "1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7"
li_input = list(map(int, input_text.split(',')))

N = max(li_input)

tree = [[] for x in range(N+1)]

for i in range(0, len(li_input), 2):
    tree[li_input[i]].append(li_input[i+1])

visited = [False] * (N+1)

queue = [1]
visited[1] = True
result = ""

while queue:
    node = queue.pop(0)
    result += f"{node}-"
    for t in tree[node]:
        if not visited[t]:
            queue.append(t)
            visited[t] = True

print(result)