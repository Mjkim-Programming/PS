"""
BOJ 24052번 Blobsad에 대한 풀이 코드.
https://www.acmicpc.net/problem/24502
"""

N, K = map(int, input().split())
blobs = list(map(int, input().split()))
t = 0
"""
모든 쌍을 탐색하며 그리디하게 옮길 양을 계산한다.
이때 blobs[i] % K는 어차피 언젠가 처리되어야 할 잔여량이기에 계속해서 오른쪽으로 넘긴다
끌어오는 것과 보내는 것의 차이는 시간에만 적용한다.
"""
for i in range(N-1):
    blobs[i+1] += blobs[i] % K
    if (blobs[i] % K)*2 < K:
        """
        blobs[i] % K가 K/2보다 작으면 보내는 게 유리하다.
        """
        t += blobs[i] % K
    else:
        """
        blobs[i] % K가 K/2보다 크면 끌어오는 게 유리하다.
        """
        t += K - blobs[i] % K
if blobs[-1] % K != 0:
    print("blobsad")
else:
    print(t)