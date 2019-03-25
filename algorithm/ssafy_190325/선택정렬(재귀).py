def select_sort(li, i):
    if i == len(li)-2:
        pass
    else:
        min_idx = i
        for j in range(i+1,len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        
        li[i], li[min_idx] = li[min_idx], li[i]
        select_sort(li, i+1)

def select_sort2(li, i):
    if i == len(li)-2:
        pass
    else:
        min_idx = li.index(min(li))
        li[i], li[min_idx] = li[min_idx], li[i]
        select_sort(li, i+1)

li = [9,8,7,6,5,4,3,2,1]

# select_sort(li, 0)
select_sort2(li, 0)

print(li)