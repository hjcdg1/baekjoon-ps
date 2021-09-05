from sys import stdin


N = int(stdin.readline())
A = [None] + list(map(int, stdin.readline().split()))

# D[i] : A[i]가 마지막인 가장 긴 증가하는 부분 수열의 길이
D = [None] + [0 for _ in range(N)]

D[1] = 1

for i in range(2, N + 1):
	D[i] = 1
	for j in range(1, i):
		if A[j] < A[i] and D[j] + 1 > D[i]:
			D[i] = D[j] + 1

print(max(D[1:]))

"""
<Another Solution>

import bisect

vector = [A[1]]
for i in range(2, N + 1):
	if A[i] > vector[-1]:
		vector.append(A[i])
	else:
		# vector[i] : 현재까지 만들 수 있는, i번째 요소가 가장 작은 길이가 (i + 1)인 증가 수열의 i번째 요소
		vector[bisect.bisect_left(vector, A[i])] = A[i]

print(len(vector))
"""
