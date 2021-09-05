from sys import stdin


N = int(stdin.readline())
A = [None] + list(map(int, stdin.readline().split()))

# D[i] : A[i]가 마지막인 증가하는 부분 수열의 합 최대값
D = [None] + [0 for _ in range(N)]

D[1] = A[1]

for i in range(2, N + 1):
	D[i] = A[i]
	for j in range(1, i):
		if A[j] < A[i] and D[j] + A[i] > D[i]:
			D[i] = D[j] + A[i]

print(max(D[1:]))
