import itertools


def check(num):
    if num[0]+1 == num[1] and num[1]+1 == num[2]:
        return True
    elif num[0] == num[1] == num[2]:
        return True
    else:
        return False


def baby_gin(num):
    for i1 in range(6):
        for i2 in range(6):
            if i2 != i1:
                for i3 in range(6):
                    if i3 != i2 and i3 != i1:
                        for i4 in range(6):
                            if i4 != i3 and i4 != i2 and i4 != i1:
                                for i5 in range(6):
                                    if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                        for i6 in range(6):
                                            if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1:
                                                if check([num[i1],num[i2],num[i3]]) and check([num[i4],num[i5],num[i6]]):
                                                    return 'Baby-gin 입니다.'
    return 'Baby-gin이 아닙니다.'


def baby_gin2(num, n,k):
    if k == n:
        if check(num[:3]) and check(num[3:]):
            return 'Baby-gin 입니다.'

    else:
        for i in range(k, n):
            num[k], num[i] = num[i], num[k]
            baby_gin2(num, n, k+1)
            num[k], num[i] = num[i], num[k]


def baby_gin3(num):
    result = list(itertools.permutations(num))

    for r in result:
        if check(r[:3]) and check(r[3:]):
            return 'Baby-gin 입니다.'

    return 'Baby-gin이 아닙니다.'


num = [0,5,4,0,6,0]

print(baby_gin(num))
print(baby_gin2(num, 6,0))
print(baby_gin3(num))
