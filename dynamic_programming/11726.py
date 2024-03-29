from sys import stdin


N = int(stdin.readline())

# D[i] : 2 x i 크기의 직사각형을 1 x 2, 2 x 1 타일로 채우는 방법의 수
D = [0 for _ in range(N + 2)]

D[1] = 1
D[2] = 2

for i in range(3, N + 1):
	D[i] = (D[i - 1] + 2 * D[i - 2] - D[i - 2]) % 10007

print(D[N])
