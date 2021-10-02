from sys import stdin


N = int(stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(N):
	a, b, c, d = list(map(int, stdin.readline().split()))
	A.append(a)
	B.append(b)
	C.append(c)
	D.append(d)

CD_dict = {}
for i in range(N):
	for j in range(N):
		cd = C[i] + D[j]
		if cd in CD_dict:
			CD_dict[cd] += 1
		else:
			CD_dict[cd] = 1

answer = 0
for i in range(N):
	for j in range(N):
		ab = A[i] + B[j]
		if -ab in CD_dict:
			answer += CD_dict[-ab]

print(answer)
