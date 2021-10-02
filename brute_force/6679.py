def get_digit_sum(number, base):
	result = 0
	n = number
	while n > 0:
		result += n % base
		n = n // base
	return result

for number in range(1000, 10000):
	sum_10 = get_digit_sum(number, 10)
	sum_12 = get_digit_sum(number, 12)
	sum_16 = get_digit_sum(number, 16)
	if sum_10 == sum_12 == sum_16:
		print(number)
