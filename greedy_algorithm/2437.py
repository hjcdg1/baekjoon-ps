# Tray again

import sys


N = int(sys.stdin.readline())
W = sorted(list(map(int, sys.stdin.readline().split())))

if W[0] != 1:
	print(1)
else:
	answer = None
	total = W[0]
	for w in W[1:]:
		if w <= total + 1:
			total += w
		else:
			answer = total + 1
			break
	if answer is None:
		answer = total + 1

	print(answer)