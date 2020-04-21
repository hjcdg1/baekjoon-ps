from sys import stdin


T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]

max_N = max(N)

# D[i] : f(i)를 호출했을 때 0과 1이 출력되는 개수
D = [None] * (max_N + 2)

D[0] = (1, 0)
D[1] = (0, 1)

for i in range(2, max_N + 1):
	D[i] = (D[i - 1][0] + D[i - 2][0], D[i - 1][1] + D[i - 2][1])

for n in N:
	print(D[n][0], D[n][1])