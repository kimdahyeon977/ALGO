import sys

input = sys.stdin.readline

t = int(input())

arr = []

for _ in range(t):
    arr.append(list(map(int, input().split())))
    
def divide(k, start_c, start_r, size, answer):
    sx = start_r + k // 3 * size #수식 두개 바뀌어도 상관 x
    sy = start_c + k % 3 * size
    val = arr[sy][sx]
    print(sx, sy, size)
    for i in range(sy, sy + size):
        for j in range(sx, sx + size):
            print(i,j)
            if val != arr[i][j]:  
                for part in range(9):
                    answer = divide(part, sy, sx, size // 3, answer)
                return answer

    answer[val + 1] += 1
    return answer

output = divide(0, 0, 0, t, [0,0,0])
for i in output:
    print(i)