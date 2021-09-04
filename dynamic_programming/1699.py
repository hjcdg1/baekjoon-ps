from sys import stdin


def is_square(n):
    return int(n ** 0.5) ** 2 == n

N = int(stdin.readline())
N_square_list = [n for n in range(1, N + 1) if is_square(n)]

# D[i] : 자연수 i에 대한 답
D = [None] + [0 for _ in range(N)]

D[1] = 1

for i in range(2, N + 1):
	if is_square(i):
		D[i] = 1
	else:
		D[i] = i
		for n in N_square_list:
			if i < n:
				break
			if D[i - n] + 1 < D[i]:
				D[i] = D[i - n] + 1

print(D[N])
