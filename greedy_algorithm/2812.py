# Try again

from sys import stdin


N, K = tuple(map(int, stdin.readline().split()))
number = list(map(int, list(stdin.readline().rstrip())))

k = 0
stack = []
for n in number:
	while k < K and stack and stack[-1] < n:
		stack.pop()
		k += 1
	stack.append(n)

print(int(''.join(map(str, stack[:N - K]))))