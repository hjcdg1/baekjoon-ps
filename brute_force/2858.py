from sys import stdin
import math


R, B = list(map(int, stdin.readline().split()))

area = R + B

for long_side in range(math.ceil(area ** (1/2)), area + 1):
	if area % long_side == 0:
		short_side = area // long_side
		if short_side < 3:
			continue
		elif 2 * long_side + 2 * (short_side - 2) == R:
			print('{} {}'.format(long_side, short_side))
			break
