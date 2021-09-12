from sys import stdin, setrecursionlimit


setrecursionlimit(1000000000)

N = int(stdin.readline())
neighbor = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	v1, v2 = list(map(int, stdin.readline().split()))
	neighbor[v1].append(v2)
	neighbor[v2].append(v1)

# D[i][0] : i번 정점에서 출발할 때 (i번 정점이 얼리 어답터가 아닌 경우)
# D[i][1] : i번 정점에서 출발할 때 (i번 정점이 얼리 어답터인 경우)
D = [[-1, -1] for _ in range(N + 1)]

# V[i] : i번 정점의 방문 여부
V = [False for _ in range(N + 1)]

def get_D(i, j):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if D[i][j] >= 0:
		return D[i][j]

	# D[i][j]의 최초 1회 계산
	else:
		V[i] = True

		# i번 정점이 얼리 어답터가 아닌 경우
		if j == 0:
			D[i][j] = 0
			for v in neighbor[i]:
				if not V[v]:
					D[i][j] += get_D(v, 1)

		# i번 정점이 얼리 어답터인 경우
		else:
			D[i][j] = 1
			for v in neighbor[i]:
				if not V[v]:
					D[i][j] += min(get_D(v, 0), get_D(v, 1))

		V[i] = False
		return D[i][j]

print(min(get_D(1, 0), get_D(1, 1)))
