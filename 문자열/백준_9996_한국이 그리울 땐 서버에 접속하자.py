from collections import deque
n = int(input())
first_check, second_check = map(str, input().split("*"))
patterns = []
flag1 = 1
for _ in range(n):
    patterns.append(input())
# print(first_check, second_check)
# print(patterns)
first_check = deque(first_check)
second_check = deque(second_check)

for pattern in patterns:
    queue = deque(pattern)
    tmp_first = first_check.copy()
    tmp_second = second_check.copy()
    flag1 = 1
    # print(queue, tmp_first, tmp_second)
    while tmp_first:
        if len(queue) == 0:
            print("NE")
            flag1 = 0
            break
        if tmp_first.popleft() == queue.popleft():
            continue
        else:
            flag1 = 0
            print("NE")
            break
    while tmp_second and flag1:
        if len(queue) == 0:
            print("NE")
            flag1 = 0
            break
        if tmp_second.pop() == queue.pop():
            continue
        else:
            flag1 = 0
            print("NE")
            break
    if flag1:
        print("DA")
