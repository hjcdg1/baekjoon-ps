# Try again

from sys import stdin


N = int(stdin.readline().rstrip())
D = [list(map(int, stdin.readline().split())) for _ in range(N)]
to_be_deleted = [[False for _ in range(N)] for _ in range(N)]

for k in range(N):
	for i in range(N):
		for j in range(N):
			if i == j or to_be_deleted[i][j]:
				continue

			if D[i][k] + D[k][j] < D[i][j]:
				print(-1)
				exit(0)

			if (D[i][k] + D[k][j] == D[i][j]) and (D[i][k] > 0) and (D[k][j] > 0):
				to_be_deleted[i][j] = True

total = 0
for i in range(N):
	for j in range(N):
		if i <= j:
			continue
		if not to_be_deleted[i][j]:
			total += D[i][j]

print(total)