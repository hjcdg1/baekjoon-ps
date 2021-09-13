from sys import stdin


N = list(map(int, stdin.readline().rstrip()))

if 0 not in N or sum(N) % 3 != 0:
	print(-1)
else:
	N.sort(reverse=True)
	print(''.join(map(str, N)))
