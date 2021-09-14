from sys import stdin


N, M = list(map(int, stdin.readline().split()))
P = [list(map(int, stdin.readline().split())) for _ in range(M)]

package_min = min([p[0] for p in P])
single_min = min([p[1] for p in P])

answer = min(package_min, single_min * 6) * (N // 6) + min(package_min, single_min * (N % 6))
print(answer)
