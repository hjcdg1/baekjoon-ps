exp = input()
exp_trimmed = [sum(map(int, plus_chunk.split('+'))) for plus_chunk in exp.split('-')]
result = exp_trimmed[0] - sum(exp_trimmed[1:])
print(result)