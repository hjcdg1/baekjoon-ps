from sys import stdin


N = int(stdin.readline())

if N < 10:
	print(0)

else:
	# D[i][j][stat] : 마지막 수가 j인 i자리의 계단 수 개수 (stat : 사용된 숫자)
	D = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N + 1)]

	for j in range(1, 10):
		D[1][j][1 << j] = 1

	for i in range(2, N + 1):
		for j in range(10):
			for stat in range(1 << 10):
				if not (stat & (1 << j)):
					continue

				if j >= 1:
					D[i][j][stat] += (
						D[i - 1][j - 1][stat] +  # j가 포함된 경우
						D[i - 1][j - 1][stat ^ (1 << j)]  # j가 포함되지 않은 경우
					)

				if j <= 8:
					D[i][j][stat] += (
						D[i - 1][j + 1][stat] +  # j가 포함된 경우
						D[i - 1][j + 1][stat ^ (1 << j)]  # j가 포함되지 않은 경우
					)

				D[i][j][stat] = D[i][j][stat] % 1000000000

	print(sum([D[N][j][(1 << 10) - 1] for j in range(10)]) % 1000000000)
