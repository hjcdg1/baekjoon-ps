from sys import stdin


T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]
max_N = max(N)

# D[i] : koong(i)의 값
D = [0 for _ in range(max_N + 4)]

D[0] = D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, max_N + 1):
	D[i] = D[i - 1] + D[i - 2] + D[i - 3] + D[i - 4]

for t in range(T):
	print(D[N[t]])