m, n, k = map(int, input().split())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False] * n for _ in range(m)]
result = []
cnt = 0
# (0, 2, 4, 4) -> (2,0 / 3,0 / 2,1 / 3,1 / 2,2 / 3,2 / 2,3 / 3,3)
for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for y in range(left_y, right_y):
        for x in range(left_x, right_x):
            graph[y][x] = 1

def dfs(y, x):
    if graph[y][x] == 1:
        return

    graph[y][x] = 1
    global area
    area += 1

    for dy, dx in move:
        if 0 <= y + dy < m and 0 <= x + dx < n:
            y = y + dy
            x = x + dx
            dfs(y, x)
    return area





for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            print("enter", y, x)
            area = 0
            area = dfs(y, x)
            result.append(area)
print(sorted(result))