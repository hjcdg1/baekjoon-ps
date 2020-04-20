from sys import stdin


S = list(map(int, list(stdin.readline().rstrip())))

stack = []

cnt_0, cnt_1 = 0, 0
if S[0] == 0:
	stack.append(0)
	cnt_0 += 1
else:
	stack.append(1)
	cnt_1 += 1

for b in S[1:]:
	if b != stack[-1]:
		stack.append(b)
		if b == 0:
			cnt_0 += 1
		else:
			cnt_1 += 1

print(min(cnt_0, cnt_1))