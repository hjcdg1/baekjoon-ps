A, B = tuple(map(list, input().split()))

A_len = len(A)
B_len = len(B)
start, end = 0, A_len - 1

min_cnt = A_len
while end < B_len:
	cnt = 0
	for i in range(start, end + 1):
		if A[i - start] != B[i]:
			cnt += 1
	if cnt < min_cnt:
		min_cnt = cnt
	start += 1
	end += 1
print(min_cnt)