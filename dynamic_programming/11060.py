from sys import stdin


N = int(stdin.readline())
A = [0] + list(map(int, stdin.readline().split()))

# D[i] : i번째 칸에서 출발할 때 필요한 최소 점프 횟수
D = [0 for _ in range(N + 1)]

for i in reversed(range(1, N)):
	if A[i] == 0:
		D[i] = -1
	else:
		D[i] = float('inf')
		for j in range(1, A[i] + 1):
			if i + j <= N and D[i + j] != -1:
				D[i] = min(D[i], D[i + j] + 1)
		D[i] = D[i] if D[i] != float('inf') else -1

print(D[1])
