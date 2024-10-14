cnt = int(input())
n = int(input())
graph = [[] * (cnt + 1) for _ in range(cnt + 1)]
visited = [False] * (cnt + 1)
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(g, v,visited):
    global cnt
    visited[v] = True

    for i in g[v]:
        if not visited[i]:
            cnt += 1
            dfs(g, i, visited)
    return cnt


result= dfs(graph, 1, visited)
print(result)
