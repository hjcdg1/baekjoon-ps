from sys import stdin


N, M = list(map(int, stdin.readline().split()))
A = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]
B = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]

cnt = 0
for i in range(N-2):
	for j in range(M-2):
		if A[i][j] != B[i][j]:
			for p in range(3):
				for q in range(3):
					A[i + p][j + q] = 0 if A[i + p][j + q] == 1 else 1
			cnt += 1

is_matched = True
for i in range(N):
	for j in range(M):
		if A[i][j] != B[i][j]:
			is_matched = False
			break

print(cnt if is_matched else -1)
