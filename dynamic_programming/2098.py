from sys import stdin


N = int(stdin.readline())
W = [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][stat] : 지금까지 방문한 도시가 stat일 때, 0번 도시로 가는 데 드는 최소 비용
D = [[0 for _ in range(1 << N)] for _ in range(N)]

def get_D(i, stat):
	if D[i][stat] != 0:
		return D[i][stat]
	else:
		# 모든 도시 방문 완료
		if stat == (1 << N) - 1:
			if W[i][0] != 0:
				D[i][stat] = W[i][0]
				return D[i][stat]
			else:
				return float('inf')

		# 방문할 도시 남음
		else:
			min_D = float('inf')
			for j in range(N):
				if (i == j) or (stat & (1 << j)) or (W[i][j] == 0):  # 방문 가능한 인접 도시 j
					continue
				min_D = min(min_D, get_D(j, stat | (1 << j)) + W[i][j])
			D[i][stat] = min_D
			return D[i][stat]

print(get_D(0, 1))