from sys import stdin


C = [None] + list(stdin.readline().rstrip())
C_len = len(C) - 1

# D[i] : C[-i] ~ C[-1] 암호의 해석 가짓수
D = [0 for _ in range(C_len + 1)]

D[0] = 1
D[1] = 1 if C[-1] != '0' else 0

for i in range(2, C_len + 1):
	if C[-i] == '0':
		continue

	D[i] = D[i - 1]
	if 10 <= int(C[-i] + C[-i + 1]) <= 26:
		D[i] += D[i - 2]
	D[i] = D[i] % 1000000

print(D[C_len])
