from sys import stdin


# Try again

N = int(stdin.readline())
W = int(stdin.readline())
P = [-1] + [tuple(map(int, stdin.readline().split())) for _ in range(W)]

# D[i][j] : 첫 번째 경찰차가 i번째 사건의 위치, 두 번째 경찰차가 j번째 사건의 위치에 있을 때
D = [[0 for _ in range(W + 1)] for _ in range(W + 1)]
S = [[None for _ in range(W + 1)] for _ in range(W + 1)]

def get_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for i in reversed(range(W)):
	for j in reversed(range(W)):
		if i == j and i != 0:
			continue
		m = max(i, j)
		d1 = get_distance(P[m + 1], P[i] if i != 0 else (1, 1))
		d2 = get_distance(P[m + 1], P[j] if j != 0 else (N, N))
		if d1 + D[m + 1][j] <= d2 + D[i][m + 1]:
			D[i][j] = d1 + D[m + 1][j]
			S[i][j] = (1, m + 1, j)
		else:
			D[i][j] = d2 + D[i][m + 1]
			S[i][j] = (2, i, m + 1)

print(D[0][0])

s, e = 0, 0
while not (s == W or e == W):
	print(S[s][e][0])
	s, e = S[s][e][1], S[s][e][2]