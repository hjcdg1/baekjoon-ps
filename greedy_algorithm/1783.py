from sys import stdin


N, M = list(map(int, stdin.readline().split()))

# 이동 불가
if N == 1:
	print(1)

# 2번과 3번을 번갈아 사용
elif N == 2:
	print(min((M - 1) // 2, 3) + 1)

# 어차피 1번 ~ 4번을 모두 사용할 수 없음
# 1번과 4번을 번갈아 사용 (단, 최대 이동 횟수는 3회)
elif M < 7:
	print(min(M - 1, 3) + 1)

# 2번과 3번을 먼저 소모하고, 1번과 4번을 번갈아 사용
else:
	print(M - 2)
