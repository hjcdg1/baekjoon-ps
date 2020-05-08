from sys import stdin


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

# D[i] : i번째 칸에서 출발할 때 필요한 최소 점프 횟수
D = [-1 for _ in range(N)]

D[N - 1] = 0
for i in reversed(range(N - 1)):
	if A[i] == 0:
		D[i] = -1
	else:
		min_D = float('inf')
		for j in range(1, A[i] + 1):
			if i + j < N and D[i + j] != -1:
				min_D = min(min_D, D[i + j])
		D[i] = min_D + 1 if min_D != float('inf') else -1

	print("D[{}] = {}".format(i, D[i]))

print(D[0])