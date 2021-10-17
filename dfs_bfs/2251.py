from sys import stdin
from collections import deque
from itertools import permutations


A, B, C = list(map(int, stdin.readline().split()))
ABC = [A, B, C]

queue = deque()
visit = [[[False for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(A + 1)]
answer = set()

queue.append((0, 0, C))
visit[0][0][C] = True
answer.add(C)

while queue:
	a, b, c = queue.popleft()

	for src, dst in permutations([0, 1, 2], 2):
		abc = [a, b, c]
		if abc[src] > 0 and abc[dst] < ABC[dst]:
			move_amount = min(abc[src], ABC[dst] - abc[dst])
			abc[src] -= move_amount
			abc[dst] += move_amount
			if not visit[abc[0]][abc[1]][abc[2]]:
				queue.append(tuple(abc))
				visit[abc[0]][abc[1]][abc[2]] = True
				if abc[0] == 0:
					answer.add(abc[2])

print(*sorted(list(answer)))
