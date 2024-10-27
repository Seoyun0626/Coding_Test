# 안전 지대 : 영역 > 비
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
info = []
result = []
max_height = 0
for _ in range(n):
    tmp_info = list(map(int, input().split()))
    max_height = max(max_height, max(tmp_info))
    info.append(tmp_info)
# print(info)
# print(max_height)

def dfs(y, x, height):
    visited[y][x] = True
    for dy, dx in move:
        if 0 <= y + dy < n and 0 <= x + dx < n and info[y + dy][x + dx] > height and not visited[y + dy][x + dx]:
            visited[y + dy][x + dx] = True
            dfs(y + dy, x + dx, height)

for i in range(0, max_height + 1):
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if info[y][x] > i and not visited[y][x]:
                dfs(y, x, i)
                cnt += 1
    result.append(cnt)
# print(result)
print(max(result))
