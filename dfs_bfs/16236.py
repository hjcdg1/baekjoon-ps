from sys import stdin
from collections import deque


def has_fish_to_eat(size):
	min_fish = None
	for fish_num, fish_cnt in enumerate(fish_cnt_list[1:], start=1):
		if fish_cnt > 0:
			min_fish = fish_num
			break

	return min_fish is not None and min_fish < size

def move(shark, size, remaining_cnt):
	queue = deque([(shark[0], shark[1], size, remaining_cnt, 0)])
	visit = [[False for _ in range(N)] for _ in range(N)]

	# 먹을 수 있는 물고기
	fish_to_eat = None

	while queue:
		# i, j : 현재 아기 상어 위치
		# s : 현재 아기 상어 크기
		# r : 성장을 위해 먹어야 하는 물고기 수
		# depth : 이동 거리
		i, j, s, r, depth = queue.popleft()
		if visit[i][j]:
			continue

		visit[i][j] = True

		# 더 먼 거리에 있는 물고기를 먹을 필요는 없음
		if fish_to_eat and depth >= fish_to_eat['depth']:
			break

		# 위쪽, 왼쪽, 아래쪽, 오른쪽 이동
		for new_i, new_j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
			if 0 <= new_i <= N - 1 and 0 <= new_j <= N - 1 and not visit[new_i][new_j]:
				# 단순 이동
				if G[new_i][new_j] in (0, s):
					queue.append((new_i, new_j, s, r, depth + 1))

				# 물고기를 먹으며 이동
				elif G[new_i][new_j] < s:
					if fish_to_eat is None or (
						new_i < fish_to_eat['new_i'] or
						(new_i == fish_to_eat['new_i'] and new_j < fish_to_eat['new_j'])
					):
						fish_to_eat = {
							'new_i': new_i,
							'new_j': new_j,
							'new_s': (s + 1) if r == 1 else s,
							'new_r': (s + 1) if r == 1 else (r - 1),
							'depth': depth + 1
						}

	# 먹을 수 있는 물고기가 있는 경우
	if fish_to_eat:
		new_i = fish_to_eat['new_i']
		new_j = fish_to_eat['new_j']
		new_s = fish_to_eat['new_s']
		new_r = fish_to_eat['new_r']
		depth = fish_to_eat['depth']

		# 물고기 수 갱신
		fish_cnt_list[G[new_i][new_j]] -= 1

		# 물고기 먹기
		G[new_i][new_j] = 0

		# 이동 거리 갱신
		global answer
		answer += depth

		return (new_i, new_j), new_s, new_r

	# 먹을 수 있는 물고기가 없는 경우
	else:
		return None, None, None

N = int(stdin.readline())
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

fish_cnt_list = [0 for _ in range(7)]  # 물고기 수
shark = None  # 아기 상어 위치
for i in range(N):
	for j in range(N):
		if 1 <= G[i][j] <= 6:
			fish_cnt_list[G[i][j]] += 1
		elif G[i][j] == 9:
			G[i][j] = 0
			shark = (i, j)
size = 2  # 아기 상어 크기
remaining_cnt = 2  # 성장을 위해 먹어야 하는 물고기 수

answer = 0
while has_fish_to_eat(size):
	shark, size, remaining_cnt = move(shark, size, remaining_cnt)
	if shark is None:
		break

print(answer)
