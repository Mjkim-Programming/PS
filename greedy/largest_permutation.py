def naive_solution(A, B):
    """
    가장 간단하게 생각할 수 있는 답안.
    O(B * N)
    
    :param A: 주어진 permutation
    :param B: 사용 가능한 swap 횟수
    """
    arr = A[:]
    for i in range(B):
        head = i
        biggest = head + arr[head:].index(max(arr[head:]))
        arr[head], arr[biggest] = arr[biggest], arr[head]
    return arr

def optimized_solition(A, B):
    """
    각각의 값이 와야 할 위치는 정해져 있다는 사실을 이용한 풀이.
    이를 로그 시간으로 낮추려면 세그먼트 트리 등의 추가적인 트릭이 필요할 것으로 보인다.
    (최적화에는 실패)
    O(n^2)
    
    :param A: 주어진 permutation
    :param B: 사용 가능한 swap 횟수
    """
    arr = A[:]
    n = len(arr)
    used = [False] * n
    order = sorted(
        [(v, i) for v, i in enumerate(arr)],
        reverse=True
    )
    for i in range(n):
        if B == 0:
            break
        for v, j in order:
            if not used[j] and j >= i and arr[i] < v:
                arr[i], arr[j] = arr[j], arr[i]
                used[j] = True
                B -= 1
                break
    return arr
    

A = list(map(int, input().split()))
B = int(input())

print(naive_solution(A, B))