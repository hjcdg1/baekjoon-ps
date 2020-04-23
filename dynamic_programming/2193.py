from sys import stdin


N = int(stdin.readline())

# D[i][0] : 0으로 끝나는 i자리 이친수의 개수
# D[i][1] : 1로 끝나는 i자리 이친수의 개수
D = [None] * (N + 1)

D[1] = (0, 1)

for i in range(2, N + 1):
	D[i] = (D[i - 1][0] + D[i - 1][1], D[i - 1][0])

print(D[N][0] + D[N][1])