import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
info = []
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
check = []
max_cnt = 1

r, c = map(int, input().split())
for _ in range(r):
    info.append(list(input().rstrip()))
print(info)

visited = [[False for _ in range(c)] for _ in range(r)]

def dfs(y, x, cnt):
    # print("enter dfs", y, x, cnt)
    global max_cnt
    check.append(info[y][x])
    visited[y][x] = True
    # print("가능한 좌표", check, visited, y, x)
    if max_cnt < cnt:
        max_cnt = cnt

    for dy, dx in move:
        if 0 <= y + dy < r and 0 <= x + dx < c and info[y + dy][x + dx] not in check and not visited[y + dy][x + dx]:
            dfs(y + dy, x + dx, cnt + 1)
            visited[y + dy][x + dx] = False
            check.pop()
dfs(0, 0, 1)
print(max_cnt)

