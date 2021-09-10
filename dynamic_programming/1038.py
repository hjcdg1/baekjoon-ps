from sys import stdin


N = int(stdin.readline())

# C[k] : 10개에서 순서 상관 없이 k개를 뽑는 경우의 수
C = [0, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

if N <= 9:
	print(N)

elif N >= sum(C[1:]):
	print(-1)

else:
	# D[i][j] : i자리의 감소하는 수 중 j번째 수
	D = [[0 for _ in range(C[i] + 1)] for i in range(11)]

	for j in range(1, C[1] + 1):
		D[1][j] = j - 1

	cnt = 10
	for i in range(2, 11):
		for j in range(1, C[i] + 1):
			if j == 1:
				D[i][j] = int(''.join(map(str, reversed(range(i)))))

			else:
				prev_str = str(D[i][j - 1])
				prev_len = len(prev_str)

				for idx in reversed(range(prev_len)):
					if idx == 0 or int(prev_str[idx - 1]) > int(prev_str[idx]) + 1:
						D[i][j] = int(
							prev_str[:idx] +
							str(int(prev_str[idx]) + 1) +
							(str(D[(prev_len - 1) - idx][1]) if idx < prev_len - 1 else '')
						)
						break

			cnt += 1
			if cnt == N + 1:
				print(D[i][j])
				break

		if cnt == N + 1:
			break
