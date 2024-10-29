import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
info = []
alpha = [False] * 26
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
max_cnt = 1
r, c = map(int, input().split())
for _ in range(r):
    info.append(list(input().rstrip()))
def dfs(y, x, cnt):
    # print("enter dfs", y, x, cnt)
    global max_cnt
    # print("가능한 좌표", check, visited, y, x)
    max_cnt = max(max_cnt, cnt)
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]

        if 0 <= ny < r and 0 <= nx < c:
            if not alpha[info[ny][nx]]:
                alpha[info[ny][nx]] = True
                dfs(ny, nx, cnt + 1)
                alpha[info[ny][nx]] = False
alpha[info[0][0]] = True
dfs(0, 0, 1)
print(max_cnt)