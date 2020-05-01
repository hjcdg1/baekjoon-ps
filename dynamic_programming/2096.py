from sys import stdin


N = int(stdin.readline())
P = [list(map(int, stdin.readline().split())) for _ in range(N)]

# MAX[i][j], MIN[i][j] : i번째 행에 숫자가 j번째 칸에 위치하는 경우 (슬라이딩 윈도우 : 메모리 절약)
MAX = [0, 0, 0]
MIN = [0, 0, 0]

MAX[0] = MIN[0] = P[0][0]
MAX[1] = MIN[1] = P[0][1]
MAX[2] = MIN[2] = P[0][2]

for i in range(1, N):
	max0 = max(MAX[0], MAX[1]) + P[i][0]
	max1 = max(MAX[0], MAX[1], MAX[2]) + P[i][1]
	max2 = max(MAX[1], MAX[2]) + P[i][2]
	MAX[0], MAX[1], MAX[2] = max0, max1, max2

	min0 = min(MIN[0], MIN[1]) + P[i][0]
	min1 = min(MIN[0], MIN[1], MIN[2]) + P[i][1]
	min2 = min(MIN[1], MIN[2]) + P[i][2]
	MIN[0], MIN[1], MIN[2] = min0, min1, min2

print(max(MAX), min(MIN))