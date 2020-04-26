from sys import stdin


N = int(stdin.readline())
A = [None] + list(map(int, stdin.readline().split()))

# D[i] : A[i]가 마지막인 증가 부분 수열의 합 최대값
D = [0 for _ in range(N + 1)]

D[1] = A[1]

for i in range(2, N + 1):
	max_D = A[i]
	for j in range(1, i):
		if A[j] < A[i]:
			max_D = max(max_D, D[j] + A[i])
	D[i] = max_D

print(max(D[1:]))