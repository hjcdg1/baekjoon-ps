from sys import stdin

T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]

max_N = max(N)

# D[i] : P(i)
D = [0 for _ in range(max_N + 5)]

D[1] = 1
D[2] = 1
D[3] = 1
D[4] = 2
D[5] = 2

for i in range(6, max_N + 1):
	D[i] = D[i - 1] + D[i - 5]

for n in N:
	print(D[n])
