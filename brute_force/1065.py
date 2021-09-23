from sys import stdin


N = int(stdin.readline())

answer = 0
for n in range(1, N + 1):
	n_str = str(n)
	n_len = len(n_str)

	if n_len <= 2:
		answer += 1
	else:
		gaps = set([int(n_str[idx]) - int(n_str[idx + 1]) for idx in range(n_len - 1)])
		if len(gaps) == 1:
			answer += 1

print(answer)
