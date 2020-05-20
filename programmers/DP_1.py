def solution(N, number):
    D = [set() for _ in range(9)]

    D[1].add(N)
    for i in range(2, 9):
        D[i].add(int(str(N) * i))
        for j in range(1, i):
            for d1 in D[j]:
                for d2 in D[i - j]:
                    D[i].add(d1 + d2)
                    D[i].add(d1 - d2)
                    D[i].add(d1 * d2)
                    if d2 != 0:
                        D[i].add(d1 // d2)

        if number in D[i]:
            return i
    return -1