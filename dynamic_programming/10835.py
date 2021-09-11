from sys import stdin


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

# D[i][j] : 왼쪽에는 i번째 카드가, 오른쪽에는 j번째 카드가 맨 위에 있을 때 게임을 시작하는 경우
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in reversed(range(N)):
	for j in reversed(range(N)):
		D[i][j] = max(D[i + 1][j], D[i + 1][j + 1])
		if A[i] > B[j]:
			D[i][j] = max(D[i][j], D[i][j + 1] + B[j])

print(D[0][0])
