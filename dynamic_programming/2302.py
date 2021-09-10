from sys import stdin


N = int(stdin.readline())
M = int(stdin.readline())
F = [int(stdin.readline()) for _ in range(M)]

# V[i] : i번의 VIP 여부
V = [False for _ in range(N + 1)]
for f in F:
	V[f] = True

# D[i][0] : i번 자리까지 고려할 때, i번이 제자리에 위치할 때의 경우의 수
# D[i][1] : i번 자리까지 고려할 때, i번이 왼쪽에 위치할 때의 경우의 수
D = [[0, 0] for _ in range(N + 1)]

D[1][0] = 1

for i in range(2, N + 1):
	D[i][0] = sum(D[i - 1])
	if not V[i] and not V[i - 1]:
		D[i][1] = D[i - 1][0]

print(sum(D[N]))
