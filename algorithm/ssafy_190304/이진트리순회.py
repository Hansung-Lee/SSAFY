def preorder(node):
    print(node, end=" ")
    for t in tree[node]:
        if t < node:
            preorder(t)
        else:
            preorder(t)

def inorder(node):
    for t in tree[node]:
        if t < node:
            inorder(t)
        print(node, end=" ")
        if t > node:
            inorder(t)

def postorder(node):
    for t in tree[node]:
        if t < node:
            postorder(t)
        else:
            postorder(t)
    print(node, end=" ")

# V = int(input())
# edges = list(map(int, input().split()))

V = 13
edges = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

tree = [[] for _ in range(V+1)]

for i in range(0, len(edges), 2):
    tree[edges[i]].append(edges[i+1])

degree = [0] * (V+1)

for node in tree:
    for x in node:
        degree[x] += 1

root = 0

for i in range(1, len(degree)):
    if degree[i] == 0:
        root = i
        break

print("Pre-order:", end=" ")
preorder(root)
print('')

print("In-order:", end=" ")
inorder(root)
print('')

print("Post-order:", end=" ")
postorder(root)
print('')