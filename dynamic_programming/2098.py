from sys import stdin


N = int(stdin.readline())
W = [list(map(int, stdin.readline().split())) for _ in range(N)]

# D[i][stat] : 지금까지 방문한 도시가 stat일 때, i번 도시에서 출발하는 경우
# 어차피 사이클을 이루기 때문에, 처음에는 0번 도시에서 출발한다고 가정해도 됨
D = [[0 for _ in range(1 << N)] for _ in range(N)]

def get_D(i, stat):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if D[i][stat] > 0:
		return D[i][stat]

	# D[i][stat]의 최초 1회 계산
	else:
		# 모든 도시 방문
		if stat == (1 << N) - 1:
			D[i][stat] = W[i][0] if W[i][0] > 0 else float('inf')
			return D[i][stat]

		D[i][stat] = float('inf')
		for j in range(N):
			if W[i][j] == 0 or (stat & (1 << j)):
				continue
			D[i][stat] = min(D[i][stat], W[i][j] + get_D(j, stat | (1 << j)))
		return D[i][stat]

print(get_D(0, 1))
