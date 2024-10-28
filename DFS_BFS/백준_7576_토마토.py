# 1 : 토마토, 0: 익지 않은 토마토, -1 : 토마토 없음
from collections import deque
import sys
input = sys. stdin.readline
sys.setrecursionlimit(10**5)
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt = 0

n, m = map(int, input().split())
info = []
for _ in range(m):
    info.append(list(map(int, input().split())))
visited = [[False for _ in range(n)] for _ in range(m)]
# print(visited)

def bfs(info1):
    global cnt
    queue = deque()
    # print("enter bfs", info1)

    for tmp_info1 in info1:
        # print(tmp_info1)
        queue.append(tmp_info1)
        y, x = tmp_info1
        visited[y][x] = True
        # print("now queue", queue)

    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            if 0 <= y + dy < m and 0 <= x + dx < n and not visited[y + dy][x + dx] and info[y + dy][x + dx] == 0:
                info[y + dy][x + dx] = 1


## '1'좌표 저장 함수
def check1():
    tmp_check1 = []
    for y in range(m):
        for x in range(n):
            if info[y][x] == 1 and not visited[y][x]:
                tmp_check1.append([y, x])
    return tmp_check1

## 종료 체크 함수
def isFinished():
    for y in range(m):
        for x in range(n):
           if info[y][x] == 0:
               return False
    return True

while not isFinished():
    result = check1()
    if len(result) == 0:
        print("-1")
        exit(0)
    else:
        cnt += 1
        bfs(result)
print(cnt)