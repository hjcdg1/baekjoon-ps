from sys import stdin
from collections import deque


M, N = list(map(int, stdin.readline().split()))
G = [list(map(int, stdin.readline().split())) for _ in range(N)]

zero_cnt = 0
queues = [deque([])]  # depth별로 큐를 따로 할당

for i in range(N):
	for j in range(M):
		if G[i][j] == 0:
			zero_cnt += 1
		elif G[i][j] == 1:
			spreadable = False
			if i > 0 and G[i - 1][j] == 0:
				spreadable = True
			elif j > 0 and G[i][j - 1] == 0:
				spreadable = True
			elif i < N - 1 and G[i + 1][j] == 0:
				spreadable = True
			elif j < M - 1 and G[i][j + 1] == 0:
				spreadable = True

			if spreadable:
				queues[0].append((i, j))

# 전파 불가
if not queues[0]:
	print(-1 if zero_cnt > 0 else 0)

# 전파 가능 (1과 0이 최소한 한 개씩은 존재)
else:
	depth = 0  # 첫 번째 depth를 0으로 정의

	while True:
		curr_queue = queues[depth]  # 현재 depth의 큐
		next_queue = deque([])  # 다음 depth의 큐

		while curr_queue:
			r, c = curr_queue.popleft()

			# depth가 0이라면, 미방문 상태의 1을 방문하는 경우라서 별도의 처리가 필요 없음
			if depth > 0:
				# 이미 방문한 경우
				if G[r][c] == 1:
					continue

				# 0을 1로 바꿔주기
				G[r][c] = 1
				zero_cnt -= 1

				# 0이 모두 사라지면 완료
				if zero_cnt == 0:
					print(depth)
					exit(0)

			# 전파 가능한 주변 칸 탐색
			if r > 0 and G[r - 1][c] == 0:
				next_queue.append((r - 1, c))
			if c > 0 and G[r][c - 1] == 0:
				next_queue.append((r, c - 1))
			if r < N - 1 and G[r + 1][c] == 0:
				next_queue.append((r + 1, c))
			if c < M - 1 and G[r][c + 1] == 0:
				next_queue.append((r, c + 1))

		if next_queue:
			queues.append(next_queue)
			depth += 1
		else:
			print(-1)
			break
