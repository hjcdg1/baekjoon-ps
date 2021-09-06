from sys import stdin


N, K = list(map(int, stdin.readline().split()))
C = [0] + [int(stdin.readline()) for _ in range(N)]

# D[i][j] : 최대 i번째 동전까지만 사용하여 j원을 만드는 경우의 수
# D[j]로 최적화 (슬라이딩 윈도우 : 메모리 절약)
D = [0 for _ in range(K + 1)]

D[0] = 1

for i in range(1, N + 1):
	for j in range(1, K + 1):
		if C[i] <= j:
			D[j] += D[j - C[i]]

print(D[K])
