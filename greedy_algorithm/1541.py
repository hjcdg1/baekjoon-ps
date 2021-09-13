from sys import stdin


E = stdin.readline().rstrip()

E_processed = [sum(map(int, chunk.split('+'))) for chunk in E.split('-')]
print(E_processed[0] - sum(E_processed[1:]))
