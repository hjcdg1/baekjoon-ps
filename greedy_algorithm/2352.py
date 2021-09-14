from sys import stdin
import bisect


N = int(stdin.readline())
P = [0] + list(map(int, stdin.readline().split()))

vector = [P[1]]
for i in range(2, N + 1):
	if vector[-1] < P[i]:
		vector.append(P[i])
	else:
		vector[bisect.bisect_left(vector, P[i])] = P[i]

print(len(vector))
