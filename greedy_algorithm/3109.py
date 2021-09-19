from sys import stdin


R, C = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(R)]

answer = 0
for r in range(R):
	stack = [(r, 0)]

	while stack:
		curr_r, curr_c = stack.pop()
		G[curr_r][curr_c] = 'x'

		if curr_c == C - 1:
			answer += 1
			break

		if curr_r < R - 1 and G[curr_r + 1][curr_c + 1] != 'x':
			stack.append((curr_r + 1, curr_c + 1))
		if G[curr_r][curr_c + 1] != 'x':
			stack.append((curr_r, curr_c + 1))
		if curr_r > 0 and G[curr_r - 1][curr_c + 1] != 'x':
			stack.append((curr_r - 1, curr_c + 1))

print(answer)
