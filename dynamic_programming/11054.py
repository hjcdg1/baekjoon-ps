from sys import stdin


N = int(stdin.readline())
A = [None] + list(map(int, stdin.readline().split()))

# D[i][0] : A[i]로 끝나는 가장 긴 바이토닉 수열의 길이 (감소 형태)
# D[i][1] : A[i]로 끝나는 가장 긴 바이토닉 수열의 길이 (증가 형태)
D = [None] + [[0, 0] for _ in range(N)]

D[1][0] = 1
D[1][1] = 1

for i in range(2, N + 1):
	D[i][0] = 1
	D[i][1] = 1
	for j in range(1, i):
		if A[i] < A[j] and (D[j][0] + 1 > D[i][0] or D[j][1] + 1 > D[i][0]):
			D[i][0] = max(D[j][0] + 1, D[j][1] + 1)
		if A[i] > A[j] and D[j][1] + 1 > D[i][1]:
			D[i][1] = D[j][1] + 1

print(max([max(d) for d in D[1:]]))
