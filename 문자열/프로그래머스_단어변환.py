import sys

sys.setrecursionlimit(10 ** 6)

result = []


def solution(begin, target, words):
    answer = 0

    visited = [False] * len(words)

    ## dfs 발생할 수 없는 상황
    if target not in words:
        return answer

    def dfs(word, depth):
        if word == target:
            result.append(depth)
            return

        for i in range(len(words)):
            if visited[i] == True:
                continue

            if checkdiff(word, words[i]) == 1:
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False

    dfs(begin, 0)
    answer = min(result)

    return answer


def checkdiff(word, target):
    diff = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            diff += 1
    return diff