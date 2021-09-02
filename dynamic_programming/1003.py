from sys import stdin


T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]

max_N = max(N)

# D[i][0] : f(i)를 호출했을 때 0이 출력되는 개수
# D[i][1] : f(i)를 호출했을 때 1이 출력되는 개수
D = [[0, 0] for _ in range(max_N + 2)]

D[0][0] = 1
D[0][1] = 0
D[1][0] = 0
D[1][1] = 1

for i in range(2, max_N + 1):
	D[i][0] = D[i - 1][0] + D[i - 2][0]
	D[i][1] = D[i - 1][1] + D[i - 2][1]

for n in N:
	print(D[n][0], D[n][1])
