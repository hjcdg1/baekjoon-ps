from sys import stdin


N = int(stdin.readline())
A = [500, 100, 50, 10, 5, 1]

answer = 0
k = 1000 - N
for a in A:
	answer += k // a
	k = k % a

print(answer)
