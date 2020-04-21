from sys import stdin


N = int(stdin.readline())

# D[i] : i를 1로 만드는 연산의 최소 횟수
D = [-1] * (N + 1)

D[1] = 0

for i in range(2, N + 1):
	candidates = []

	if i % 3 == 0:
		candidates.append(D[i // 3])
	if i % 2 == 0:
		candidates.append(D[i // 2])
	candidates.append(D[i - 1])

	D[i] = min(candidates) + 1

print(D[N])