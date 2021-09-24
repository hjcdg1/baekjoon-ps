from sys import stdin


N = int(stdin.readline())
WH = [list(map(int, stdin.readline().split())) for _ in range(N)]

rank = [0 for _ in range(N)]

for i in range(N):
	cnt = 0
	for j in range(N):
		if i == j:
			continue
		if WH[j][0] > WH[i][0] and WH[j][1] > WH[i][1]:
			cnt += 1
	rank[i] = cnt + 1

print(' '.join(map(str, rank)))
