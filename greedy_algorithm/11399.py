N = int(input())
P = list(map(int, input().split()))

result = sum(P)
for i, p in enumerate(sorted(P)[:-1]):
	result += p * (N-1-i)
print(result)