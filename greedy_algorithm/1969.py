from sys import stdin


N, M = list(map(int, stdin.readline().split()))
DNAs = [stdin.readline().rstrip() for _ in range(N)]

result_DNA = []
result_diff = 0

for idx in range(M):
	cnt_dict = {}
	for c in [DNA[idx] for DNA in DNAs]:
		if c not in cnt_dict:
			cnt_dict[c] = 0
		cnt_dict[c] += 1

	max_cnt = 0
	selected_c = None
	for c, cnt in cnt_dict.items():
		if cnt > max_cnt or (cnt == max_cnt and c < selected_c):
			max_cnt = cnt
			selected_c = c

	result_DNA.append(selected_c)
	result_diff += len(list(filter(lambda c: c != selected_c, [DNA[idx] for DNA in DNAs])))

print(''.join(result_DNA))
print(result_diff)
