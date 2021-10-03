from sys import stdin


def dfs(i, j, move, percentage):
	global answer

	# N번 이동 완료
	if move == N:
		answer += percentage

	# 추가 이동 필요
	else:
		if (i, j + 1) not in visit:
			visit.add((i, j + 1))
			dfs(i, j + 1, move + 1, percentage * (P_E / 100))
			visit.remove((i, j + 1))

		if (i, j - 1) not in visit:
			visit.add((i, j - 1))
			dfs(i, j - 1, move + 1, percentage * (P_W / 100))
			visit.remove((i, j - 1))

		if (i + 1, j) not in visit:
			visit.add((i + 1, j))
			dfs(i + 1, j, move + 1, percentage * (P_S / 100))
			visit.remove((i + 1, j))

		if (i - 1, j) not in visit:
			visit.add((i - 1, j))
			dfs(i - 1, j, move + 1, percentage * (P_N / 100))
			visit.remove((i - 1, j))

N, P_E, P_W, P_S, P_N = list(map(int, stdin.readline().split()))

visit = {(0, 0)}
answer = 0
dfs(0, 0, 0, 1)

print(answer)
