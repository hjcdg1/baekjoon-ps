from sys import stdin


def get_diff(C, x, y):
	result = float('inf')

	# 흰 칸으로 시작하는 체스판과 비교
	cnt = 0
	for i in range(8):
		for j in range(8):
			if (i + j) % 2 == 0 and C[x + i][y + j] == 'B':
				cnt += 1
			elif (i + j) % 2 == 1 and C[x + i][y + j] == 'W':
				cnt += 1
	result = min(result, cnt)

	# 검은 칸으로 시작하는 체스판과 비교
	cnt = 0
	for i in range(8):
		for j in range(8):
			if (i + j) % 2 == 0 and C[x + i][y + j] == 'W':
				cnt += 1
			elif (i + j) % 2 == 1 and C[x + i][y + j] == 'B':
				cnt += 1
	result = min(result, cnt)

	return result


N, M = list(map(int, stdin.readline().split()))
C = [list(stdin.readline().rstrip()) for _ in range(N)]

answer = float('inf')
for i in range(N - 7):
	for j in range(M - 7):
		answer = min(answer, get_diff(C, i, j))

print(answer)
