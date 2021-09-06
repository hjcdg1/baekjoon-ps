from sys import stdin


N = int(stdin.readline())
C = [0] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][0/1/2] : i번 집을 R/G/B로 칠하는 경우의 비용 최솟값 (i번 집까지만 칠할 때)
D = [[0, 0, 0] for _ in range(N + 1)]

D[1][0] = C[1][0]
D[1][1] = C[1][1]
D[1][2] = C[1][2]

for i in range(2, N + 1):
	D[i][0] = C[i][0] + min(D[i - 1][1], D[i - 1][2])
	D[i][1] = C[i][1] + min(D[i - 1][0], D[i - 1][2])
	D[i][2] = C[i][2] + min(D[i - 1][0], D[i - 1][1])

print(min(D[N]))
