from sys import stdin


DOC = stdin.readline().rstrip()
W = stdin.readline().rstrip()

DOC_len = len(DOC)
W_len = len(W)

idx = 0
answer = 0

while idx < DOC_len:
	if DOC[idx:idx + W_len] == W:
		answer += 1
		idx += W_len
	else:
		idx += 1

print(answer)
