from sys import stdin


N, K = list(map(int, stdin.readline().split()))
A = [int(stdin.readline()) for _ in range(N)]

answer = 0
k = K
for a in reversed(A):
	answer += k // a
	k = k % a

print(answer)
