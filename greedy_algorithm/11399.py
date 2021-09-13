from sys import stdin


N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

answer = sum(P)
for idx, p in enumerate(sorted(P)[:-1]):
	answer += p * (N - idx - 1)

print(answer)
