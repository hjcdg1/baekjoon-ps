from sys import stdin


N, M = list(map(int, stdin.readline().split()))
J = int(stdin.readline())
P = [int(stdin.readline()) for _ in range(J)]

start = 1
end = M
answer = 0

for p in P:
	if start <= p <= end:
		continue

	if end < p:
		move = p - end
	else:
		move = p - start

	start += move
	end += move
	answer += abs(move)

print(answer)
