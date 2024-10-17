from collections import deque
import sys

input = sys.stdin.readline

result = [] # 각 사람에 대해 단계 수 저장
n, m = map(int, input().split())
info = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    info[a].append(b)
    info[b].append(a)
# print(info)

def bfs(v, visited):
    deq = deque([v])
    visited[v] = 0

    while deq:
        num = deq.popleft()
        for tmp_num in info[num]:
            if visited[tmp_num] == 0 and tmp_num != v:
                visited[tmp_num] += (visited[num] + 1)
                deq.append(tmp_num)
    return sum(visited)

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    tmp_result = bfs(i, visited)
    result.append(tmp_result)
# print(result)

result = result.index(min(result)) + 1
print(result)