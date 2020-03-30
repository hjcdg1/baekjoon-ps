import sys


K = int(sys.stdin.readline())
A = sys.stdin.readline().split()

NUMBER_ASC, NUMBER_DESC = list(range(10)), list(reversed(range(10)))
result_max, result_min = [], []
cnt_max, cnt_min = 0, 0

for a in A:
	if a == '<':
		cnt_max += 1

		if cnt_min > 0:
			min_number = NUMBER_DESC.pop()
			numbers_to_insert = [NUMBER_DESC.pop() for _ in range(cnt_min)]
			numbers_to_insert.reverse()
			result_min.extend(numbers_to_insert)
			result_min.append(min_number)
			cnt_min = 0
		else:
			result_min.append(NUMBER_DESC.pop())
	elif a == '>':
		cnt_min += 1

		if cnt_max > 0:
			max_number = NUMBER_ASC.pop()
			numbers_to_insert = [NUMBER_ASC.pop() for _ in range(cnt_max)]
			numbers_to_insert.reverse()
			result_max.extend(numbers_to_insert)
			result_max.append(max_number)
			cnt_max = 0
		else:
			result_max.append(NUMBER_ASC.pop())

if cnt_min > 0:
	min_number = NUMBER_DESC.pop()
	numbers_to_insert = [NUMBER_DESC.pop() for _ in range(cnt_min)]
	numbers_to_insert.reverse()
	result_min.extend(numbers_to_insert)
	result_min.append(min_number)
else:
	result_min.append(NUMBER_DESC.pop())

if cnt_max > 0:
	max_number = NUMBER_ASC.pop()
	numbers_to_insert = [NUMBER_ASC.pop() for _ in range(cnt_max)]
	numbers_to_insert.reverse()
	result_max.extend(numbers_to_insert)
	result_max.append(max_number)
else:
	result_max.append(NUMBER_ASC.pop())

print(''.join(map(str, result_max)))
print(''.join(map(str, result_min)))