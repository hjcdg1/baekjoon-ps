# Try again

from sys import stdin


N = int(stdin.readline())
TP = [None] + [tuple(map(int, stdin.readline().split())) for _ in range(N)]

# D[i] : i일 상담이 마지막일 때의 최대 이익 (i일 상담 불가 : -1)
D = [-1] * (N + 1)

D[1] = TP[1][1] if TP[1][0] <= N else -1

for i in range(2, N + 1):
	if i + TP[i][0] - 1 > N:
		D[i] = -1
	else:
		max_D = TP[i][1]
		for j in range(1, i):
			if D[j] != -1 and j + TP[j][0] - 1 < i:
				max_D = max(max_D, D[j] + TP[i][1])
		D[i] = max_D

answer = 0
for i in range(1, N + 1):
	answer = max(answer, D[i])
print(answer)