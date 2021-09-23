from sys import stdin


N = int(stdin.readline())
C = [stdin.readline().rstrip() for _ in range(N)]

answer = ''

# KBS1을 찾고 첫 번째 위치로 올림
KBS1_idx = C.index('KBS1')
answer += '1' * KBS1_idx + '4' * KBS1_idx
C.insert(0, C.pop(KBS1_idx))

# KBS2를 찾고 두 번째 위치로 올림
KBS2_idx = C.index('KBS2')
answer += '1' * KBS2_idx + '4' * (KBS2_idx - 1)

print(answer)
