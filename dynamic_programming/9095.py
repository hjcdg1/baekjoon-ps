from sys import stdin


T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]

max_N = max(N)

# D[i] : 정수 i를 1, 2, 3의 합으로 나타내는 경우의 수
D = [-1] * (max_N + 3)

D[1] = 1
D[2] = 2
D[3] = 4

for i in range(4, max_N + 1):
	D[i] = D[i - 1] + D[i - 2] + D[i - 3]

for n in N:
	print(D[n])