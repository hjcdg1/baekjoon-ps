from sys import stdin


N = int(stdin.readline().rstrip())
D = [list(map(int, stdin.readline().split())) for _ in range(N)]

to_be_deleted = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
	for j in range(N):
		# 양방향 그래프이므로 한 쪽만 고려
		if i >= j:
			continue

		# 또 다른 도시 k를 방문하는 경우 고려
		for k in range(N):
			if k == i or k == j:
				continue

			if D[i][k] + D[k][j] == D[i][j]:
				to_be_deleted[i][j] = True
				break
			elif D[i][k] + D[k][j] < D[i][j]:
				print(-1)
				exit(0)

answer = 0
for i in range(N - 1):
	for j in range(i + 1, N):
		if not to_be_deleted[i][j]:
			answer += D[i][j]

print(answer)
