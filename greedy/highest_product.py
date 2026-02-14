import time
import sys

def wrong_naive_solution(arr):
    """
    정렬을 활용한 (진짜로) 단순한 해답. (단, len(arr) >= 3이라고 가정한 상태)
    최대값을 만들어내는 세 수에 음수가 들어가는 테스트케이스는 통과하지 못한다.
    O(n log n)
    :param arr: 숫자 리스트
    """
    arr2 = arr[:]
    arr2.sort()
    if not len(arr2) >= 3:
        raise ValueError(f"주어진 숫자의 개수는 3개 이상이어야 합니다. 입력된 개수 : {len(arr2)}개")
    res = arr2[-1] * arr2[-2] * arr2[-3]
    return res

def naive_solution(arr):
    """
    정렬을 활용한 비교적 단순한 해답. (단, len(arr) >= 3이라고 가정한 상태)
    O(n log n)
    :param arr: 숫자 리스트
    """
    arr2 = arr[:]
    arr2.sort()
    if not len(arr2) >= 3:
        raise ValueError(f"주어진 숫자의 개수는 3개 이상이어야 합니다. 입력된 개수 : {len(arr2)}개")
    res = max(arr2[-1] * arr2[-2] * arr2[-3], arr2[0]*arr2[1]*arr2[-1])
    return res

def optimized_solution(arr):
    """
    조금 더 복잡한 해답.
    가장 큰쪽에서 K개의 값, 가장 작은쪽에서 K개의 값은 정렬 없이도 관리할 수 있다.
    O(n)
    :param arr: 숫자 리스트
    """
    if not len(arr) >= 3:
        raise ValueError(f"주어진 숫자의 개수는 3개 이상이어야 합니다. 입력된 개수 : {len(arr2)}개")
    max1 = max2 = max3 = -sys.maxsize
    min1 = min2 = sys.maxsize
    for x in arr:
        if x > max1:
            max3 = max2
            max2 = max1
            max1 = x
        elif x > max2:
            max3 = max2
            max2 = x
        elif x > max3:
            max3 = x
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x
    return max(max1*max2*max3, min1*min2*max1)

arr = list(map(int, input().split()))
arr1 = arr[:]
arr2 = arr[:]
arr3 = arr[:]

start = time.perf_counter()
r1 = naive_solution(arr1)
t1 = time.perf_counter() - start

start = time.perf_counter()
r2 = optimized_solution(arr2)
t2 = time.perf_counter() - start

start = time.perf_counter()
r3 = wrong_naive_solution(arr2)
t3 = time.perf_counter() - start

print(f"Wrong Naive Result : {r3}")
print(f"Fixed Naive Result : {r1}")
print(f"Optimized Result : {r2}")
print(f"Wrong Naive Time : {t3}")
print(f"Fixed Naive Time : {t1}")
print(f"Optimized Time : {t2}")