# 1 : 토마토, 0: 익지 않은 토마토, -1 : 토마토 없음
from collections import deque
import sys
input = sys. stdin.readline
sys.setrecursionlimit(10**5)
check1 = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

n, m = map(int, input().split())
info = []
queue = deque()
for _ in range(m):
    info.append(list(map(int, input().split())))
max_day = 0

for y in range(m):
    for x in range(n):
        if info[y][x] == 1:
            queue.append((y, x, 0)) # 좌표 + 날짜 추가

while queue:
    y, x, day = queue.popleft()
    # print("y, x, day", y, x, day)
    if max_day < day:
        max_day = day
    for dy, dx in move:
        if 0 <= y + dy < m and 0 <= x + dx < n and info[y + dy][x + dx] == 0:
            queue.append((y + dy, x + dx, day + 1))
            info[y + dy][x + dx] = 1

for row in info:
    if 0 in row:
        print(-1)
        exit(0)
print(max_day)