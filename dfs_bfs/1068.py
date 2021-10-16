from sys import stdin


def calculate_leaf_cnt(v):
	# 값이 결정되어 있다면 굳이 다시 계산하지 않음
	if C[v] > 0:
		return C[v]

	# C[v]의 최초 1회 계산
	else:
		if not children[v]:
			C[v] = 1
			return C[v]

		result = 0
		for cv in children[v]:
			result += calculate_leaf_cnt(cv)
		C[v] = result
		return C[v]

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
D = int(stdin.readline())

root = None
children = [[] for _ in range(N)]
for v, p in enumerate(P):
	if p == -1:
		root = v
	else:
		children[p].append(v)

# C[v] : v번 노드가 루트인 서브 트리의 리프 노드 개수
C = [0 for _ in range(N)]

# 총 리프 노드 개수 계산
total_leaf_cnt = calculate_leaf_cnt(root)

if D == root:
	print(0)
elif len(children[P[D]]) >= 2:
	print(total_leaf_cnt - C[D])
else:
	print(total_leaf_cnt - C[D] + 1)
