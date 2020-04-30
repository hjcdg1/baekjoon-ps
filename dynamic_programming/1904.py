# Try again

from sys import stdin


N = int(stdin.readline())

# D[i] : 길이가 i인 것에 대한 답 (슬라이딩 윈도우 : 메모리 절약)
D = [0, 1, 2]

if N == 1:
	print(1)
else:
	for _ in range(3, N + 1):
		D1, D2 = D[1], D[2]
		D[1], D[2] = D2, (D1 + D2) % 15746

	print(D[2] % 15746)