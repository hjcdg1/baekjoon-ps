from sys import stdin


N = int(stdin.readline())
A = [-1] + list(map(int, stdin.readline().split()))

# D[i] : A[i]로 끝나는 최장 부분 감소 수열의 길이
D = [0 for _ in range(N + 1)]

D[1] = 1

for i in range(2, N + 1):
	max_D = 1
	for j in range(1, i):
		if A[j] > A[i]:
			max_D = max(max_D, D[j] + 1)
	D[i] = max_D

print(max(D[1:]))