N, K = tuple(map(int, input().split()))
A = [int(input()) for _ in range(N)]

result = 0
R = K
for a in reversed(A):
	result += R // a
	R = R % a
print(result)