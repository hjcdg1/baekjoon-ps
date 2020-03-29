N = list(map(int, input()))

if 0 not in N:
	print(-1)
elif sum(N) % 3 != 0:
	print(-1)
else:
	print(''.join(map(str, sorted(N, reverse=True))))