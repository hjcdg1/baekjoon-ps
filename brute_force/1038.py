from sys import stdin
from itertools import combinations


N = int(stdin.readline())

if N < 10:
	print(N)

elif N >= sum([len(list(combinations(range(10), i))) for i in range(1, 11)]):
	print(-1)

else:
	# D[i] : i번째 감소하는 수
	D = [0 for _ in range(N + 1)]

	# M[i] : 자릿수가 i인 가장 작은 감소하는 수
	M = [0 for _ in range(11)]

	for i in range(10):
		D[i] = i
	M[2] = 10

	for i in range(10, N + 1):
		prev_D_str = str(D[i - 1])
		prev_D_len = len(prev_D_str)

		for idx in range(prev_D_len - 1, -1, -1):
			if idx == 0 and prev_D_str[idx] == '9':
				D[i] = int(''.join(map(str, reversed(range(prev_D_len + 1)))))
				M[prev_D_len + 1] = D[i]
				break

			elif idx == 0 or int(prev_D_str[idx - 1]) > int(prev_D_str[idx]) + 1:
				D_str = prev_D_str[:idx]
				D_str += str(int(prev_D_str[idx]) + 1)
				if idx < prev_D_len - 1:
					D_str += str(M[prev_D_len - idx - 1])
				D[i] = int(D_str)
				break

	print(D[N])
