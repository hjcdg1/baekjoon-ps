from sys import stdin


S = list(stdin.readline().rstrip())

cnt_dict = {}
for char in S:
	if char in cnt_dict:
		cnt_dict[char] += 1
	else:
		cnt_dict[char] = 1

center = None
has_palindrome = True
neighbor_chars = []
for char, cnt in cnt_dict.items():
	if cnt % 2 == 0:
		neighbor_chars.extend([char] * (cnt // 2))
	else:
		if center is None:
			center = char
			neighbor_chars.extend([char] * (cnt // 2))
		else:
			has_palindrome = False
			break

if not has_palindrome:
	print('I\'m Sorry Hansoo')
else:
	neighbor_chars.sort()
	answer = ''.join([
		''.join(neighbor_chars),
		center if center else '',
		''.join(reversed(neighbor_chars))
	])
	print(answer)
