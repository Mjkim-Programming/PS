def naive_solution(A):
    """
    O(n log n)으로 추정
    
    :param A: 회의의 시작시간과 끝 시간이 짝지어서 주어진 리스트
    """
    dat = []
    for s, e in A:
        dat.append((s, +1))
        dat.append((e, -1))
    dat.sort()
    curr = 0
    maxM = 0
    for _, v in dat:
        curr += v
        maxM = max(maxM, curr)
    return maxM

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
    
print(naive_solution(A))