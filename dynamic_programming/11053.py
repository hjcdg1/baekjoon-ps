from sys import stdin


N = int(stdin.readline())
A = [-1] + list(map(int, stdin.readline().split()))

# D[i] : A[i]가 마지막 수인 LIS 길이
D = [-1] * (N + 1)

D[1] = 1

for i in range(2, N + 1):
	max_D = 1
	for j in range(1, i):
		if A[j] < A[i] and D[j] + 1 > max_D:
			max_D = D[j] + 1
	D[i] = max_D

max_D = -1
for i in range(1, N + 1):
	if D[i] > max_D:
		max_D = D[i]
print(max_D)

"""
<Another Solution>

import bisect

vector = [A[1]]
for i in range(2, N + 1):
	if A[i] > vector[-1]:
		vector.append(A[i])
	else:
		vector[bisect.bisect_left(vector, A[i])] = A[i]

print(len(vector))
"""