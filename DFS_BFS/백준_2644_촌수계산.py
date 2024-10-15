from collections import deque
n = int(input())
check1, check2 = map(int, input().split())
m = int(input())
visited = [-1] * (n + 1)
cnt = 0
flag = 0

graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(start, end, visited):
    global graph, cnt
    deq = deque([start])
    visited[start] = 0

    while deq:
        num = deq.popleft()
        for i in graph[num]:
            if visited[i] == -1:
                deq.append(i)
                visited[i]  += (visited[num] + 2)
    print(visited[end])
bfs(check1, check2, visited)


