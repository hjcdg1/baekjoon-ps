from sys import stdin


N = int(stdin.readline())
W = list(map(int, stdin.readline().split()))

W.sort()

if W[0] > 1:
	print(1)

else:
	end = 1
	answer = None

	for w in W[1:]:
		if w <= end + 1:
			end += w
		else:
			break

	print(end + 1)
