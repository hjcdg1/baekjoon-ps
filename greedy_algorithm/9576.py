import sys


T = int(sys.stdin.readline())

for _ in range(T):
	N, M = tuple(map(int, sys.stdin.readline().split()))
	AB = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

	AB.sort(key=lambda x: x[0])
	AB.reverse()

	cnt = 0
	for book in range(1, N + 1):
		if AB:
			if AB[-1][0] > book:
				continue
			else:
				while AB and AB[-1][1] < book:
					AB.pop()
				if AB:
					min_end_idx = -1
					AB_r = list(reversed(AB))
					for i, ab in enumerate(AB_r):
						if ab[0] > book:
							break
						if min_end_idx == -1 or ab[1] < AB_r[min_end_idx][1]:
							min_end_idx = i
					AB.pop(-1 - min_end_idx)
					cnt += 1
				else:
					break
		else:
			break

	print(cnt)