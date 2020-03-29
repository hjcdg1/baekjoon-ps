N = int(input())
W = [int(input()) for _ in range(N)]

W_sorted = sorted(W, reverse=True)

unit = 10000
max_w = 0
for i, w in enumerate(W_sorted):
	if w < unit:
		unit = w
	if max_w < (i + 1) * unit:
		max_w = (i + 1) * unit
print(max_w)