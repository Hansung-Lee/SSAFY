def preorder(T):
    if T:
        print(T, end=" ")
        preorder(tree[T][0])
        preorder(tree[T][1])

def inorder(T):
    if T:
        inorder(tree[T][0])
        print(T, end=" ")
        inorder(tree[T][1])

def postorder(T):
    if T:
        postorder(tree[T][0])
        postorder(tree[T][1])
        print(T, end=" ")


V = 13
edges = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

tree = [[0] * 2 for _ in range(V+1)]

for i in range(0, len(edges), 2):
    if not tree[edges[i]][0]:
        tree[edges[i]][0] = edges[i+1]
    else:
        tree[edges[i]][1] = edges[i+1]

print("Pre-order:", end=" ")
preorder(1)
print('')

print("In-order:", end=" ")
inorder(1)
print('')

print("Post-order:", end=" ")
postorder(1)
print('')