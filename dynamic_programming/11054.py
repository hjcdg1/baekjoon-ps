from sys import stdin


N = int(stdin.readline())
A = [-1] + list(map(int, stdin.readline().split()))

# D[i] : A[i]로 끝나는 가장 긴 바이토닉 수열 길이 (감소 형태, 증가 형태)
D = [[0, 0] for _ in range(N + 1)]

D[1][0] = 1
D[1][1] = 1

for i in range(2, N + 1):
	max_D0, max_D1 = 1, 1
	for j in range(1, i):
		if A[j] > A[i]:
			max_D0 = max(max_D0, D[j][0] + 1, D[j][1] + 1)
		if A[j] < A[i]:
			max_D1 = max(max_D1, D[j][1] + 1)
	D[i][0], D[i][1] = max_D0, max_D1

result = 0
for i in range(1, N + 1):
	result = max(result, D[i][0], D[i][1])
print(result)