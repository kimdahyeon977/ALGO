```
✨접근법
1. 겹칠 경우 : min_val, max_val을 계속 upate해준다. (주식 문제와 비슷)
2. 겹치지 않는 경우 : 선의 길이를 더해주소 min_val, max_val을 현재 좌표로
🤯어려웠던점
1. min_val, max_val을 맨처음 좌표로 초기화해주는 것
2. 입력은 항상 작은 순대로 주어지지 않는다.  
```
```python
'''
176112kb / 3152ms
'''
import sys

input = sys.stdin.readline

n = int(input())

origin_lines = list(tuple(map(int, input().split())) for _ in range(n))
origin_lines.sort()  #무조건 x좌표 작은순대로 정렬되어야 다음 알고리즘 성립

min_val, max_val = origin_lines[0]
answer = 0

for x,y in origin_lines[1:]:
    if x > max_val:
        answer += (max_val - min_val)
        min_val = x
        max_val = y
    else:
        min_val = min(min_val, x)
        max_val = max(max_val, y)
answer += (max_val - min_val)
print(answer)
```

        