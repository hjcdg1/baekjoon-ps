from sys import stdin


N = int(stdin.readline())

# 0의 개수, 1의 개수, ..., 9의 개수
cnt_list = [0 for _ in range(10)]

# 현재 0~9를 카운트하고 있는 자릿수 (1의 자릿수부터 시작)
digit = 1

# 현재 digit 자릿수를 카운트하려는 값들의 구간
start = 1
end = N

while True:
	# 구간 시작값의 1의 자릿수가 0이 되도록 조정
	start_last_number = start % 10
	resize_start = start
	if start_last_number != 0:
		resize_start += (10 - start_last_number)

	# 구간 종료값의 1의 자릿수가 9가 되도록 조정
	end_last_number = end % 10
	resize_end = end
	if end_last_number != 9:
		resize_end -= (end_last_number + 1)

	# 더 이상 조정이 불가능한 경우 루프 탈출
	if resize_start > resize_end:
		break

	# 구간 시작값의 조정 과정에 존재하는 값들에 대해, 카운트되지 않은 자릿수 전부 카운트
	# digit 이전 자릿수까지는 카운트가 완료된 상태
	if start_last_number != 0:
		for i in str(start)[:-1]:
			cnt_list[int(i)] += (resize_start - start) * digit
		for i in range(start_last_number, 10):
			cnt_list[i] += digit

	# 구간 종료값의 조정 과정에 존재하는 값들에 대해, 카운트되지 않은 자릿수 전부 카운트
	# digit 이전 자릿수까지는 카운트가 완료된 상태
	if end_last_number != 9:
		for i in str(end)[:-1]:
			cnt_list[int(i)] += (end - resize_end) * digit
		for i in range(0, end_last_number + 1):
			cnt_list[i] += digit

	# 조정된 구간에 존재하는 값들에 대해, digit 자릿수 전부 카운트
	# digit 이전 자릿수까지는 카운트가 완료된 상태
	for i in range(10):
		cnt_list[i] += (resize_end // 10 - resize_start // 10 + 1) * digit

	# 다음 자릿수를 카운트하기 위한 준비
	start = resize_start // 10
	end = resize_end // 10
	digit *= 10

# 남은 구간에 대해 카운트되지 않은 자릿수 전부 카운트
for i in range(start, end + 1):
	for j in str(i):
		cnt_list[int(j)] += digit

print(' '.join(map(str, cnt_list)))
