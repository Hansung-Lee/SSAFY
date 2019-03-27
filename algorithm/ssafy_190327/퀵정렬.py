def quickSort(li, l, r):
    if l < r:
        s = partition(li, l, r)
        quickSort(li, l, s - 1)
        quickSort(li, s + 1, r)


def partition(li, l, r):
    p = li[l]
    i = l
    j = r

    while i < j:
        while i < r and li[i] <= p:
            i += 1
        while j > l and li[j] >= p:
            j -= 1
        if i < j:
            li[i], li[j] = li[j], li[i]

    li[l], li[j] = li[j], li[l]

    return j


li = [9, 8, 7, 6, 5, 4, 3, 2, 1]

quickSort(li, 0, len(li)-1)

print(li)