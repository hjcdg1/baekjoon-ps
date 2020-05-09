from sys import stdin


N = int(stdin.readline())
P = [-1] + list(map(int, stdin.readline().split()))

# D[i] : P[i]가 끝인 LIS의 길이
D = [0 for _ in range(N + 1)]

D[1] = 1

for i in range(2, N + 1):
	max_D = 1
	for j in range(i):
		if P[j] < P[i]:
			max_D = max(max_D, D[j] + 1)
	D[i] = max_D

print(max(D[1:]))