class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def add(pre, data):
    global Head
    if pre == None:
        Head = Node(data, Head)
    else:
        pre.link = Node(data, pre.link)

def get(index):
    global Head
    node = Head
    for i in range(index):
        node = node.link

    return node.data

li_N = [1,5,2,4,3]

Head = Node(li_N[0], None)

for n in range(1, len(li_N)):
    pre_node = None
    node = Head
    for i in range(n):
        if li_N[n] > node.data:
            add(pre_node, li_N[n])
            break
        elif i == n:
            add(node, li_N[n])
            break
        else:
            pre_node = node
            node = node.link

result = []
for i in range(len(li_N)-1, -1, -1):
    result.append(get(i))

print(result)