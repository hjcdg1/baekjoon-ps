from sys import stdin


N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
R = list(map(int, stdin.readline().split()))

# D[i][j] = 현재 i번째 왼쪽 카드와 j번째 오른쪽 카드부터 시작할 때 얻을 수 있는 최대 점수
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in reversed(range(N)):
	for j in reversed(range(N)):
		D[i][j] = max(D[i + 1][j], D[i + 1][j + 1])
		if L[i] > R[j]:
			D[i][j] = max(D[i][j], R[j] + D[i][j + 1])

print(D[0][0])