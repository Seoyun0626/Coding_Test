import sys
input = sys.stdin.readline
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = [] # 각 단지 마자 아파트 개수 들어감
n = int(input())
info = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    info.append(input())

def dfs(y, x):
    global cnt
    visited[y][x] = True
    for dy, dx in move:
        if 0 <= y + dy < n and 0 <= x + dx < n and not visited[y + dy][x + dx] and info[y + dy][x + dx] == '1':
            cnt += 1
            dfs(y + dy, x + dx)

    return cnt

for y in range(n):
    for x in range(n):
        if not visited[y][x] and info[y][x] == '1':
            cnt = 1
            cnt = dfs(y, x)
            result.append(cnt)
result = sorted(result)
print(len(result))
for num in result:
    print(num)
