from sys import stdin


C = [None] + list(stdin.readline().rstrip())
C_len = len(C) - 1

if C[1] == '0':
	print(0)
elif C_len == 1:
	print(1)
else:
	# D[i] : C[1] ~ C[i]를 해석하는 경우의 수
	D = [0 for _ in range(C_len + 1)]

	D[1] = 1
	if C[2] == '0':
		D[2] = 1 if C[1] == '1' or C[1] == '2' else 0
	else:
		D[2] = 2 if 11 <= int(''.join(C[1:3])) <= 26 else 1

	for i in range(3, C_len + 1):
		case = 0
		if int(C[i]) != 0:
			case += D[i - 1]
		if C[i - 1] != '0' and 10 <= int(''.join(C[i - 1:i + 1])) <= 26:
			case += D[i - 2]
		D[i] = case % 1000000

	print(D[C_len])

"""
문제에서 요구하는 답이 K로 나눈 나머지라면, 점화식을 다음과 같이 수정한다.

	>> D[i] = (D[i - 1] + D[i - 2]) % K

이를 차례대로 계산하다 보면 D[i - 1]와 D[i - 2]의 합이 K보다 커지는 순간에 도달한다.
이때 D[i]에는 실제로 계산된 값이 아닌, 그것을 K로 나눈 나머지 값이 들어가게 된다.
그러면 D[i]의 값이 잘못되어 있음에도 D[i + 1]은 계산이 올바르게 이뤄질까? 그렇다.

	>> D[i + 1] = (D[i] + D[i - 1]) % K

D[i]와 D[i - 1] 자리에 실제로 계산된 값이 아닌 K로 나눈 나머지 값이 들어가 있더라도,
D[i + 1]에 들어가게 되는 우변의 연산 결과는 똑같다. 이는 나머지 연산의 성질 때문이다.
결국 이런 식으로 계속 계산하다 보면 모든 D[i]는 다음과 같은 정합성을 따르게 된다.

	>> D[i] : 실제 D[i] 값을 K로 나눈 나머지 값

따라서 최종적으로 출력해줄 때는 D[N]을 출력해주면 그만이다.
"""