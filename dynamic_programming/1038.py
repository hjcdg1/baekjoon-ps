# Try again

from sys import stdin


N = int(stdin.readline())

if N <= 10:
	print(N)

else:
	# D[i] : i번째 감소하는 수 (슬라이딩 윈도우 : 메모리 절약)
	D = 10

	for i in range(11, N + 1):
		str_list = list(str(D))
		str_len = len(str_list)

		if str_len == 10:
			D = -1
			break

		cnt = 0
		for j in reversed(range(str_len)):
			if str_list[j] != '9':
				str_list[j] = str(int(str_list[j]) + 1)
				if j == 0 or str_list[j] != str_list[j - 1]:
					break
				else:
					str_list[j] = str(cnt)
					cnt += 1
			else:
				str_list = [str(k) for k in reversed(range(str_len + 1))]
				break
		D = int(''.join(str_list))

	print(D)