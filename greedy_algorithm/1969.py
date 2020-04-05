import sys


N, M = tuple(map(int, sys.stdin.readline().split()))
DNAs = [sys.stdin.readline().rstrip() for _ in range(N)]

result_DNA = []
result_diff = 0

for i in range(M):
	cnt_dict = {}
	frequent_c = None

	for c in [DNA[i] for DNA in DNAs]:
		if c not in cnt_dict:
			cnt_dict[c] = 1
		else:
			cnt_dict[c] += 1

		if frequent_c is None:
			frequent_c = c
		elif cnt_dict[c] > cnt_dict[frequent_c]:
			frequent_c = c
		elif cnt_dict[c] == cnt_dict[frequent_c] and c < frequent_c:
			frequent_c = c

	result_DNA.append(frequent_c)
	result_diff += N - cnt_dict[frequent_c]

print(''.join(result_DNA))
print(result_diff)