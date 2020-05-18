# Try again

from sys import stdin


N = int(stdin.readline())

# D[i][e][stat] : i자리, 끝 수가 e, 사용된 숫자 상태가 stat
D = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N + 1)]

for e in range(1, 10):
	D[1][e][1 << e] = 1

for i in range(2, N + 1):
	for e in range(10):
		for stat in range(1 << 10):
			if not (stat & (1 << e)):
				continue

			if e >= 1:
				D[i][e][stat] += D[i - 1][e - 1][stat]
				D[i][e][stat] += D[i - 1][e - 1][stat ^ (1 << e)]
			if e <= 8:
				D[i][e][stat] += D[i - 1][e + 1][stat]
				D[i][e][stat] += D[i - 1][e + 1][stat ^ (1 << e)]
			D[i][e][stat] %= 1000000000

ans = 0
for e in range(10):
	ans += D[N][e][(1 << 10) - 1]
print(ans % 1000000000)