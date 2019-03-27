def backtrack(li, k, n, sum):
	if sum > 10:
		return
	if k == n:
		if sum == 10:
			for j in range(n):
				if chk[j]:
					print(li[j], end=" ")
			print()
		return

	k += 1
	
	chk[k-1] = 1
	backtrack(li, k, n, sum+li[k-1])
	chk[k-1] = 0
	backtrack(li, k, n, sum)
	
li = [1,2,3,4,5,6,7,8,9,10]
chk = [0] * len(li)
backtrack(li, 0, len(li), 0)