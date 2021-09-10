from sys import stdin


N, M, K = list(map(int, stdin.readline().split()))

# C[i][j] : i개에서 순서 상관 없이 j개를 뽑는 경우의 수
C = [[0 for _ in range(i + 1)] for i in range(N + M + 1)]

C[1][0] = 1
C[1][1] = 1

for i in range(2, N + M + 1):
	for j in range(i + 1):
		if j == 0 or j == i:
			C[i][j] = 1
		else:
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

if K > C[N + M][N]:
	print(-1)

else:
	n, m, k = N, M, K
	answer = ''

	while True:
		if n == 0:
			answer += 'z' * m
			break
		elif m == 0:
			answer += 'a' * n
			break

		break_point = C[(n - 1) + m][n - 1]
		if 1 <= k <= break_point:
			answer += 'a'
			n -= 1
		else:
			answer += 'z'
			m -= 1
			k -= break_point

	print(answer)
