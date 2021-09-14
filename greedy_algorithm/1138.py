from sys import stdin


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

idx_list = list(range(N))
sequence = [0 for _ in range(N)]

for idx, a in enumerate(A):
	sequence[idx_list[a]] = idx + 1
	idx_list.pop(a)

print(' '.join(map(str, sequence)))
