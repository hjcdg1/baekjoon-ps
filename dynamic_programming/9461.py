from sys import stdin

T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]
max_N = max(N)

# D[i] : P(i)
D = [-1] * (max_N + 5)

D[1], D[2], D[3], D[4], D[5] = 1, 1, 1, 2, 2

for i in range(6, max_N + 1):
	D[i] = D[i - 1] + D[i - 5]

for n in N:
	print(D[n])