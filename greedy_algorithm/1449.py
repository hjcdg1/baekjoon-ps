from sys import stdin


N, L = list(map(int, stdin.readline().split()))
P = list(map(int, stdin.readline().split()))

P.sort()

end = P[0] - 0.5 + L
answer = 1

for p in P[1:]:
	if p + 0.5 <= end:
		continue
	else:
		end = p - 0.5 + L
		answer += 1

print(answer)
