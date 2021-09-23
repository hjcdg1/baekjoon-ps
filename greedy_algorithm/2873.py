from sys import stdin


R, C = list(map(int, stdin.readline().split()))
P = [list(map(int, stdin.readline().split())) for _ in range(R)]

if R % 2 == 1:
	print(('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * ((R - 1) // 2) + 'R' * (C - 1))

elif C % 2 == 1:
	print(('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * ((C - 1) // 2) + 'D' * (R - 1))

else:
	"""
	격자를 체스 판처럼 생각하고, 처음 칸을 검은 칸이라고 하면 마지막 칸도 검은 칸이다.
	그리고 검은 칸에서 검은 칸으로 가려면 짝수 번의 이동이 필요하다.
	그러나 남은 모든 칸을 방문하려면 홀수 번(짝수 X 짝수 - 1)번의 이동이 필요하다.
	따라서 남은 모든 칸을 방문하는 것은 불가능하고, 최소한 하나의 칸을 버려야 한다.
	그런데 하나의 칸만 버리려면 반드시 흰 칸을 버려야 한다.
	그래야 짝수 번의 이동 과정에서 검은 칸과 흰 칸을 똑같은 횟수로 방문하기 때문이다.
	"""

	def flip_direction(d):
		if d == 'U':
			return 'D'
		elif d == 'R':
			return 'L'
		elif d == 'L':
			return 'R'
		else:
			return 'U'

	# 버릴 흰 칸 선택
	min_p = 1000
	throw_i, throw_j = None, None
	for i in range(R):
		for j in range(C):
			if (i + j) % 2 == 0:  # 검은 칸은 패스
				continue
			elif P[i][j] < min_p:
				min_p = P[i][j]
				throw_i = i
				throw_j = j

	# 버릴 칸이 짝수 번째 줄에 위치할 때
	if throw_i % 2 == 0:
		# 사람 1을 버릴 칸 바로 왼쪽에 위치시킴
		person1 = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (throw_i // 2)
		person1 += 'DRUR' * ((throw_j - 1) // 2)

		# 사람 2를 버릴 칸 바로 아래쪽에 위치시킴
		person2 = ('L' * (C - 1) + 'U' + 'R' * (C - 1) + 'U') * ((R - throw_i - 2) // 2)
		person2 += 'ULDL' * ((C - throw_j - 1) // 2)

		# 최종 경로
		answer = person1 + 'DR' + ''.join(map(flip_direction, reversed(person2)))

	# 버릴 칸이 홀수 번째 줄에 위치할 때
	else:
		# 사람 1을 버릴 칸 바로 위쪽에 위치시킴
		person1 = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * ((throw_i - 1) // 2)
		person1 += 'DRUR' * (throw_j // 2)

		# 사람 2를 버릴 칸 바로 오른쪽에 위치시킴
		person2 = ('L' * (C - 1) + 'U' + 'R' * (C - 1) + 'U') * ((R - throw_i - 1) // 2)
		person2 += 'ULDL' * ((C - throw_j - 2) // 2)

		# 최종 경로
		answer = person1 + 'RD' + ''.join(map(flip_direction, reversed(person2)))

	print(answer)
