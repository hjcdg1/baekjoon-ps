from sys import stdin


N = int(stdin.readline())
P = [None] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# MAX[i][j] : i번째 행까지만 볼 때, i번째 행에 숫자가 j번째 칸에 위치하는 경우의 최대 점수
# MAX[j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
MAX = [0, 0, 0]

# MIN[i][j] : i번째 행까지만 볼 때, i번째 행에 숫자가 j번째 칸에 위치하는 경우의 최소 점수
# MIN[j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
MIN = [0, 0, 0]

MAX[0] = MIN[0] = P[1][0]
MAX[1] = MIN[1] = P[1][1]
MAX[2] = MIN[2] = P[1][2]

for i in range(2, N + 1):
	MAX_0 = max(MAX[0], MAX[1]) + P[i][0]
	MAX_1 = max(MAX[0], MAX[1], MAX[2]) + P[i][1]
	MAX_2 = max(MAX[1], MAX[2]) + P[i][2]

	MAX[0] = MAX_0
	MAX[1] = MAX_1
	MAX[2] = MAX_2

	MIN_0 = min(MIN[0], MIN[1]) + P[i][0]
	MIN_1 = min(MIN[0], MIN[1], MIN[2]) + P[i][1]
	MIN_2 = min(MIN[1], MIN[2]) + P[i][2]

	MIN[0] = MIN_0
	MIN[1] = MIN_1
	MIN[2] = MIN_2

print(max(MAX), min(MIN))
