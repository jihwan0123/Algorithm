# 1655. 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

max_heap, min_heap, ans = [], [], []

n = int(input())
for i in range(1, n+1):
    x = int(input())

    # 홀수번째 입력은 max_heap에 삽입
    if i & 1:
        heapq.heappush(max_heap, -x)
    # 짝수번째는 min_heap에
    else:
        heapq.heappush(min_heap, x)

    # max_heap의 최대값이 min_heap의 최솟값보다 크면 heap위치를 교환해서 정렬한다
    if i >= 2 and -max_heap[0] > min_heap[0]:
        maxV = -heapq.heappop(max_heap)
        minV = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -minV)
        heapq.heappush(min_heap, maxV)
    # max_heap의 최대값이 가운데 수
    ans.append(-max_heap[0])

print('\n'.join(map(str, ans)))
