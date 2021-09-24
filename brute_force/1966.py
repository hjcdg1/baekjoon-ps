from sys import stdin


T = int(stdin.readline())
for _ in range(T):
	N, M = list(map(int, stdin.readline().split()))
	P = list(map(int, stdin.readline().split()))

	priorities = [{
		'id': idx,
		'value': p
	} for idx, p in enumerate(P)]

	answer = []
	while priorities:
		first = priorities.pop(0)
		if priorities and first['value'] < max([priority['value'] for priority in priorities]):
			priorities.append(first)
		else:
			answer.append(first)

	for idx, priority in enumerate(answer):
		if priority['id'] == M:
			print(idx + 1)
			break
