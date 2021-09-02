from sys import stdin


N = int(stdin.readline())

# D[i][0] : 0으로 끝나는 i자리 이친수의 개수
# D[i][1] : 1로 끝나는 i자리 이친수의 개수
D = [None] + [[0, 0] for _ in range(N)]

D[1][0] = 0
D[1][1] = 1

for i in range(2, N + 1):
	D[i][0] = D[i - 1][0] + D[i - 1][1]
	D[i][1] = D[i - 1][0]

print(sum(D[N]))
