```
✨ 접근법 : 간단한 구현문제
1. heapq에 우선순위 배열 담으면 간단하게 풀 수 있음.
2. 만족도 구할때 "학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다." 이 조건빼먹어서 한참 헤맴. 
```
```python
'''
128816kb / 472ms
'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

my_dict = {}

for _ in range(n ** 2):
    q = []
    num, c1, c2, c3, c4 = map(int, input().split())
    lst = [c1, c2, c3, c4]
    my_dict[num] = lst
    
    for c in range(n):
        for r in range(n):
            if arr[c][r] == 0:
                cand, empty= 0, 0
                for i in range(4):
                    ny = c + dy[i]
                    nx = r + dx[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[ny][nx] in lst:
                            cand += 1
                        if arr[ny][nx] == 0:
                            empty += 1
                heapq.heappush(q,(-cand, -empty, c, r))
    cand, _, y, x = heapq.heappop(q)
    arr[y][x] = num


total = 0
for c in range(n):
    for r in range(n):
        cnt = 0
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[ny][nx] in my_dict[arr[c][r]]:
                    cnt += 1
        total += 10 ** (cnt - 1) if cnt > 0 else 0
print(total)
```