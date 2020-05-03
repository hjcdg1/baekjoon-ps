# Try again

from sys import stdin
import bisect


N = int(stdin.readline())
C = [-1] + [int(stdin.readline()) for _ in range(N)]

vector = [C[1]]
for i in range(2, N + 1):
	if vector[-1] < C[i]:
		vector.append(C[i])
	else:
		vector[bisect.bisect_left(vector, C[i])] = C[i]
print(N - len(vector))