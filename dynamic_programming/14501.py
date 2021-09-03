from sys import stdin


N = int(stdin.readline())
TP = [None] + [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i] : i일 상담이 마지막일 때의 최대 이익 (i일 상담 불가 : 0)
D = [None] + [0 for _ in range(N)]

D[1] = TP[1][1] if TP[1][0] <= N else 0

for i in range(2, N + 1):
	if (i - 1) + TP[i][0] > N:
		D[i] = 0
		continue

	D[i] = max([TP[i][1]] + [
		TP[i][1] + D[j]
		for j in range(1, i)
		if D[j] > 0 and (j - 1) + TP[j][0] < i
	])

print(max(D[1:]))
