import sys
input = sys.stdin.readline
info = []
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 1
r, c = map(int, input().split())
for _ in range(r):
    info.append(list(input().rstrip()))
check = [0] * 26
check[ord(info[0][0]) - ord('A')] = 1
def dfs(y, x, dist, check):
    # print("enter dfs", y, x, cnt)
    global cnt
    cnt = dist
    # print("가능한 좌표", check, visited, y, x)
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if 0 <= ny < r and 0 <= nx < c:
            tmp = ord(info[ny][nx]) - ord('A')
            if not check[tmp]:
                check[tmp] = 1
                cnt = max(cnt, dfs(ny, nx, dist + 1, check))
                check[tmp] = 0
    return cnt


result = dfs(0, 0, 1, check)
print(result)