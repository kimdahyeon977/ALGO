```
✨접근법
heapq 사용하여서 정렬
출력 형태 주의하기
```
```python
'''
109240kb / 120ms
'''
import sys
import heapq
input = sys.stdin.readline

n, c = map(int, input().split())

lst = list(map(int, input().split()))

q = []

for i in set(lst):
    heapq.heappush(q, [-lst.count(i), lst.index(i), i])

answer = []

while q:
    cnt, _, val = heapq.heappop(q)
    answer.extend([val]*-cnt)

print(*answer)
```