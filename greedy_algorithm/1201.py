from sys import stdin
from collections import deque


N, M, K = tuple(map(int, stdin.readline().split()))

if not (M + K -1 <= N <= M * K):
	print(-1)

else:
	numbers = list(range(1, N + 1))

	# 덩어리 1개 (N == K)
	if M == 1:
		result = list(reversed(numbers))

	# 덩어리 2개 이상
	elif M > 1:
		if K == 1:
			result = numbers
		elif K > 1:
			result = list(reversed(numbers[:K]))

			size_per_group = round((N - K) / (M - 1))
			start = K
			group_ends = []
			while True:
				group_ends.append(start + size_per_group)
				start += size_per_group
				if len(group_ends) == M - 1:
					break

			if start < N:
				r = N - start
				for i in range(1, len(group_ends) + 1):
					group_ends[-i] += r
					r -= 1
					if r == 0:
						break

			start = K
			for group_end in group_ends:
				result += list(reversed(numbers[start:group_end]))
				start = group_end

	print(' '.join(list(map(str, result))))