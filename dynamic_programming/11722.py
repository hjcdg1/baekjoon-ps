from sys import stdin


N = int(stdin.readline())
A = [None] + list(map(int, stdin.readline().split()))

# D[i] : A[i]가 마지막인 가장 긴 감소하는 부분 수열의 길이
D = [None] + [0 for _ in range(N)]

D[1] = 1

for i in range(2, N + 1):
	D[i] = 1
	for j in range(1, i):
		if A[j] > A[i] and D[j] + 1 > D[i]:
			D[i] = D[j] + 1

print(max(D[1:]))
