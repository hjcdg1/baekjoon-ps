# Tray again

from sys import stdin
import bisect


N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

vector = [P[0]]
for p in P[1:]:
	if p > vector[-1]:
		vector.append(p)
	else:
		vector[bisect.bisect_left(vector, p)] = p
print(len(vector))