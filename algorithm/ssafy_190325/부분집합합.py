def subset(li):
    for i in range(1<<len(li)):
        temp = []
        for j in range(len(li)):
            if i & (1<<j):
                temp.append(li[j])
        if temp and sum(temp) == 0:
            print(temp)

# def subset2(li,n,r):
#     global temp
#     if r == 0:
#         print(temp)
#         temp = []
#     elif n < r:
#         return
#     else:
#         temp.append(li[n-1])
#         subset2(li, n-1, r-1)
#         subset2(li, n-1, r)



li = [-1,3,-9,6,7,-6,1,5,4,-2]

subset(li)
# subset2(li,10,9)