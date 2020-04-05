import sys


DOC = sys.stdin.readline().rstrip()
W = sys.stdin.readline().rstrip()

DOC_len = len(DOC)
W_len = len(W)

cnt = 0
i = 0
while i < DOC_len:
	if DOC[i:i + W_len] == W:
		cnt += 1
		i += W_len
	else:
		i += 1
print(cnt)