from sys import stdin


T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]

max_N = max(N)

D = [False for _ in range(max_N + 1)]
for n in range(1, max_N + 1):
	for i in range(1, max_N + 1):
		if i % n == 0:
			D[i] = not D[i]

for n in N:
	print(len(list(filter(lambda x: x, D[1:n + 1]))))
