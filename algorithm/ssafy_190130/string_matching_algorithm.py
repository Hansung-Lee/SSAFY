def BruteForce(t, p):
    N = len(t) # 전체 텍스트의 길이
    M = len(p) # 찾을 패턴의 길이
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:
        return [(i-M)] # 검색 성공
    else:
        return "not found" # 검색 실패


def partial(pattern):
    ret = [0]
    
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret
    
def kmp(T, P):
    part, ret, j = partial(P), [], 0

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = part[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P):
            ret.append(i - (j - 1))
            j = 0
    return ret


def Rabin_Karp(text, pattern, d=1, q=1):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result

def boyer_moore(text, key):
    bcs = {}

    for i in range(len(key)-1, -1, -1):
        if key[i] not in bcs.keys():
            bcs[key[i]] = len(key)-i-1

    len_text = len(text)
    len_key = len(key)
    i = len_key-1
    index = len_key -1
    j = i

    while i >= 0 and j <= len_text:
        if text[j] != key[i]:
            if text[j] not in bcs.keys():
                j += len_key
                i = index
            else:
                j += bcs[text[j]]
                i = index
        else:
            j -= 1
            i -= 1

    if j > len_text:
        return "not found"
    else:
        return [j + 1]


p = "is" # 찾을 패턴
t = "This is a book~!" # 전체 텍스트

print(BruteForce(t,p))
print(kmp(t,p))
print(Rabin_Karp(t,p))
print(boyer_moore(t,p))