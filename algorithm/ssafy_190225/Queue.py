N = 20

queue = []
cnt = [1] * N
pop = 0
i = 1

while N>0:
    if pop==0:
        queue.append([i, cnt[1]])
        print(f"{i}번 학생 : 입장하여 줄을 선다.")
        i += 1
    else:
        queue.append([pop, cnt[pop]])
        print(f"{pop}번 학생 : 다시 줄을 선다.")
        print(f"학생 줄 : {[x[0] for x in queue]}")
        queue.append([i, cnt[i]])
        print(f"===> {i}번 학생 : 입장하여 줄을 선다.")
        i += 1
    print(f"학생 줄 : {[x[0] for x in queue]}")
    pop = queue.pop(0)[0]
    print(f"{pop}번 학생 : 줄에서 나와...")
    print(f"학생 줄 : {[x[0] for x in queue]}")
    N -= cnt[pop]
    if N<0:
        num = 0-N
        cnt[pop] -= num
        N = 0
    print(f"{pop}번 학생 : 선생님한테 사탕 {cnt[pop]}개를 받는다")
    cnt[pop] += 1
    print(f"===== 남은 사탕의 개수는 {N}개다.")
    print("")