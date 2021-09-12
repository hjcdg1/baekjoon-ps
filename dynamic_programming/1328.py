from sys import stdin


N, L, R = list(map(int, stdin.readline().split()))

# D[i][l][r] : i번째 빌딩부터 고려할 때 왼쪽에서는 l개, 오른쪽에서는 r개가 보이는 경우의 수
D = [[[0 for _ in range(R + 1)] for _ in range(L + 1)] for _ in range(N + 1)]

D[N][1][1] = 1

for i in reversed(range(1, N)):
    for l in range(1, L + 1):
        for r in range(1, R + 1):
            D[i][l][r] = (
                D[i + 1][l - 1][r] +  # i번째 빌딩을 맨 왼쪽에 두는 경우
                D[i + 1][l][r - 1] +  # i번째 빌딩을 맨 오른쪽에 두는 경우
                D[i + 1][l][r] * (N - i - 1)  # i번째 빌딩을 중간에 두는 경우
            ) % 1000000007

print(D[1][L][R])
