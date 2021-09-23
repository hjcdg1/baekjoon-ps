from sys import stdin


N = int(stdin.readline())

answer = 0
for n in range(1, N + 1):
	if n + sum(map(int, list(str(n)))) == N:
		answer = n
		break

print(answer)
