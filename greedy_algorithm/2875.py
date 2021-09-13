from sys import stdin
import math


N, M, K = list(map(int, stdin.readline().split()))

team_num = math.floor(min(N, 2 * M) / 2)
remaining_num = N + M - 3 * team_num

print(team_num - math.ceil(max(K - remaining_num, 0) / 3))
