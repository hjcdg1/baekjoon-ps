from sys import stdin


N = int(stdin.readline())
W = int(stdin.readline())
P = [0] + [list(map(int, stdin.readline().split())) for _ in range(W)]

# D[i][j] : 경찰차 1이 i번째 사건의 위치, 경찰차 2가 j번째 사건의 위치에 있을 때
D = [[0 for _ in range(W + 1)] for _ in range(W + 1)]

# S[i][j] : D[i][j]의 출처(방향) (1: 경찰차 1, 2: 경찰차 2)
S = [[0 for _ in range(W + 1)] for _ in range(W + 1)]

def get_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for i in reversed(range(W)):
	for j in reversed(range(W)):
		# 일어날 수 없는 경우는 생략
		if i > 0 and i == j:
			continue

		# 처리할 사건의 번호
		event_idx = max(i, j) + 1

		# 경찰차 1, 경찰차 2의 현재 위치
		P1 = P[i] if i > 0 else [1, 1]
		P2 = P[j] if j > 0 else [N, N]

		# 경찰차 1이 처리하는 경우, 경찰차 2가 처리하는 경우
		D1 = get_distance(P1, P[event_idx]) + D[event_idx][j]
		D2 = get_distance(P2, P[event_idx]) + D[i][event_idx]

		if D1 <= D2:
			D[i][j] = D1
			S[i][j] = 1
		else:
			D[i][j] = D2
			S[i][j] = 2

print(D[0][0])
i = 0
j = 0
while not (i == W or j == W):
	event_idx = max(i, j) + 1
	if S[i][j] == 1:
		i = event_idx
		print(1)
	else:
		j = event_idx
		print(2)
