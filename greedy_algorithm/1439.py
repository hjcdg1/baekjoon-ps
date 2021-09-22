from sys import stdin


S = list(map(int, list(stdin.readline().rstrip())))

prev = S[0]
cnt = [1 if prev == 0 else 0, 1 if prev == 1 else 0]

for c in S[1:]:
	if c == prev:
		continue
	else:
		cnt[c] += 1
		prev = c

print(min(cnt))
