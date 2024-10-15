from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def dfs(v):
    global dfs_visited
    dfs_visited[v] = True
    print(v, end=" ")
    graph[v].sort()
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs_visited[i] = True
            dfs(i)
dfs(v)
print()
def bfs(v):
    global bfs_visited
    print(v, end=" ")
    bfs_visited[v] = True
    deq = deque([v])


    while deq:
        num = deq.popleft()
        graph[num].sort()
        for i in graph[num]:
            if not bfs_visited[i]:
                print(i, end=" ")
                bfs_visited[i] = True
                deq.append(i)
bfs(v)
