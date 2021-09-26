from sys import stdin


N = int(stdin.readline())

if N < 10:
	print(N)

else:
	N_len = len(str(N))

	answer = 0
	for i in range(1, N_len):
		answer += i * 9 * (10 ** (i - 1))
	answer += N_len * ((N - 10 ** (N_len - 1)) + 1)

	print(answer)
