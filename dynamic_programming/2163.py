from sys import stdin


N, M = tuple(map(int, stdin.readline().split()))
print(N * M - 1)