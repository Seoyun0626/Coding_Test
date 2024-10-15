from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if m == 0:
    print(n)
    exit(0)
graph = [[] for _ in range(n + 1)]
visited = [False] *  (n + 1)
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def bfs(v, visited):
    global graph
    deq = deque([v])
    visited[v] = True

    while deq:
        num = deq.popleft()
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)
    # print(v, visited, cnt)

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        bfs(i, visited)
print(cnt)