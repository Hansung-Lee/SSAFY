def push(S, x):
    global top

    top += 1

    if top > len(S):
        print("Overflow")
    else:
        S[top] = x


def pop(S):
    global top

    if top == -1:
        print("Underflow")
    else:
        top -= 1
        return S[top+1]


stack = [0] * 10
top = -1

push(stack, 1)
push(stack, 2)
push(stack, 3)
print(pop(stack))
print(pop(stack))
print(pop(stack))