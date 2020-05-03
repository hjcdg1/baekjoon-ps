from sys import stdin


N = int(stdin.readline())
M = int(stdin.readline())
F = [int(stdin.readline()) for _ in range(M)]

# D[i][0] : (i - 1)번까지의 자리가 결정되어 있을 때, i번이 제자리/왼쪽/오른쪽에 위치할 때의 경우의 수
D = [[0, 0, 0] for _ in range(N + 1)]

m = F.pop() if F else -1
for i in reversed(range(1, N + 1)):
	if i == N:
		if m == N:
			D[N][0] = 1
			D[N][1] = 0
			D[N][2] = 0
			m = F.pop() if F else -1
		else:
			D[N][0] = 1
			D[N][1] = 1
			D[N][2] = 0
	elif i == 1:
		if m == 1:
			D[1][0] = D[2][0] + D[2][2]
			D[1][1] = 0
			D[1][2] = 0
			m = F.pop() if F else -1
		else:
			D[1][0] = D[2][0] + D[2][2]
			D[1][1] = 0
			D[1][2] = D[2][1]
	else:
		if m == i:
			D[i][0] = D[i + 1][0] + D[i + 1][2]
			D[i][1] = 0
			D[i][2] = 0
			m = F.pop() if F else -1
		else:
			D[i][0] = D[i + 1][0] + D[i + 1][2]
			D[i][1] = D[i + 1][0] + D[i + 1][2]
			D[i][2] = D[i + 1][1]

print(D[1][0] + D[1][2])