from sys import stdin


def alphabet_to_idx(alphabet):
	return ord(alphabet) - ord('A')

def dfs(i, j):
	visit[alphabet_to_idx(G[i][j])] = True
	result = 1

	if i > 0 and not visit[alphabet_to_idx(G[i - 1][j])]:
		result = max(result, dfs(i - 1, j) + 1)
	if j > 0 and not visit[alphabet_to_idx(G[i][j - 1])]:
		result = max(result, dfs(i, j - 1) + 1)
	if i < R - 1 and not visit[alphabet_to_idx(G[i + 1][j])]:
		result = max(result, dfs(i + 1, j) + 1)
	if j < C - 1 and not visit[alphabet_to_idx(G[i][j + 1])]:
		result = max(result, dfs(i, j + 1) + 1)

	visit[alphabet_to_idx(G[i][j])] = False
	return result

R, C = list(map(int, stdin.readline().split()))
G = [list(stdin.readline().rstrip()) for _ in range(R)]

visit = [False for _ in range(26)]
print(dfs(0, 0))
