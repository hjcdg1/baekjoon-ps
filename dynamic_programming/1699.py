from sys import stdin
import bisect


def is_square(n):
	return int(n ** 0.5) ** 2 == n

def get_square_list(n):
	return [e for e in range(1, n + 1) if is_square(e)]

N = int(stdin.readline())
N_square_list = get_square_list(N)

# D[i] : 자연수 i에 대한 답
D = [0 for _ in range(N + 1)]

D[1] = 1

for i in range(2, N + 1):
	lb = bisect.bisect_left(N_square_list, i)
	end_idx = lb if is_square(i) else lb - 1

	min_D = 100001
	for s in N_square_list[:end_idx + 1]:
		min_D = min(min_D, D[i - s])
	D[i] = 1 + min_D

print(D[N])