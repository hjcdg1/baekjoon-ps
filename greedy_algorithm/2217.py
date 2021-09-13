from sys import stdin


N = int(stdin.readline())
W = [int(stdin.readline()) for _ in range(N)]

W.sort(reverse=True)

answer = W[0]
for idx, w in enumerate(W[1:]):
	answer = max(answer, w * (idx + 2))

print(answer)
