from collections import deque
n, m = map(int, input().split())
info = []
# (0, 0) -> (n - 1, m - 1)
for _ in range(n):
    info.append(input())
# print(info)
cnt = 0
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited =[[0 for _ in range(m)] for _ in range(n)]
# print(visited)

def bfs(y, x):
    global cnt
    deq = deque([(y, x)])
    visited[y][x] = 1
    # print("enter", y, x)
    while deq:
        (y, x) = deq.popleft()
        for dy, dx in move:
            if 0 <= y + dy < n and 0 <= x + dx < m:
                if info[y + dy][x + dx] == '1' and visited[y + dy][x + dx] == 0:
                    # print("enter", y + dy, x + dx)
                    visited[y + dy][x + dx] = (visited[y][x] + 1)
                    deq.append((y + dy, x + dx))
    # print(visited)


bfs(0, 0)
print(visited[n - 1][m - 1])
