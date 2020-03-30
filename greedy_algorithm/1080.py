import sys


N, M = tuple(map(int, sys.stdin.readline().split()))
A = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
B = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

cnt = 0
for i in range(N-2):
	for j in range(M-2):
		if A[i][j] != B[i][j]:
			for p in range(3):
				for q in range(3):
					A[i+p][j+q] = 0 if A[i+p][j+q] == 1 else 1
			cnt += 1

is_matched = True
for i in range(N-2, N):
	for j in range(M):
		if A[i][j] != B[i][j]:
			is_matched = False

for i in range(0, N-2):
	for j in range(M-2, M):
		if A[i][j] != B[i][j]:
			is_matched = False

if is_matched:
	print(cnt)
else:
	print(-1)