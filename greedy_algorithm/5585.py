N = int(input())
R = 1000 - N
A = [500, 100, 50, 10, 5, 1]

result = 0
for a in A:
	result += R // a
	R = R % a
print(result)