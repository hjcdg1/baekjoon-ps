N, M, K = tuple(map(int, input().split()))

number_of_teams = N // 2 if N < 2 * M else M
R = abs(N + M - 3 * number_of_teams)
if K > R:
	number_of_teams -= ((K - R - 1) // 3) + 1
print(number_of_teams)