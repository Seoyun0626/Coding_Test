n = int(input())
info = []
for _ in range(n):
    info.append(input())
dic = {}
for title in info:
    if title not in dic:
        dic[title] = 1
    else:
        dic[title] += 1
dic = dict(sorted(dic.items(), key = lambda x : x[0]))
dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse=True))
result = list(dic.keys())[0]
print(result)