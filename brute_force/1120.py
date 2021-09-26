from sys import stdin


A, B = list(map(list, stdin.readline().split()))

A_len = len(A)
B_len = len(B)

answer = float('inf')
for start_idx in range(B_len - A_len + 1):
	diff = 0
	for idx in range(A_len):
		diff += 1 if A[idx] != B[start_idx + idx] else 0
	answer = min(answer, diff)

print(answer)
