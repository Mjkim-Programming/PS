import time

def naive_solution(arr, N):
    """
    가장 직관적인 해답. O(n^2)
    :param arr: 전구의 상태 리스트(0, 1로만 이루어져 있음)
    :param N: 전구의 상태 리스트 길이
    """
    cnt = 0
    for i in range(N):
        if arr[i] == 0:
            cnt += 1
            for j in range(i, N):
                arr[j] = 1 if arr[j] == 0 else 0
    return cnt
    
def optimized_solution(arr, N):
    """
    최적화가 추가된 해답. O(n)
    :param arr: 전구의 상태 리스트(0, 1로만 이루어져 있음)
    :param N: 전구의 상태 리스트 길이
    """
    cnt = 0
    pivot = 0
    for i in range(N):
        if arr[i] == pivot:
            cnt += 1
            pivot = 1 if pivot == 0 else 0
    return cnt

arr = list(map(int, input().split()))
arr1 = arr[:]
arr2 = arr[:]
N = len(arr)

start = time.perf_counter()
r1 = naive_solution(arr1, N)
t1 = time.perf_counter() - start

start = time.perf_counter()
r2 = optimized_solution(arr2, N)
t2 = time.perf_counter() - start

print(f"Naive Result : {r1}")
print(f"Optimized Result : {r2}")
print(f"Naive Time : {t1}")
print(f"Optimized Time : {t2}")