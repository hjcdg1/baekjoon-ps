# Try again faster

import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))

index_list = list(range(N))
result = [-1 for _ in range(N)]
for i, a in enumerate(A):
	result[index_list[a]] = i + 1
	index_list.pop(a)
print(' '.join(map(str, result)))