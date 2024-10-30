n = int(input())
length = int(input())
check_length = 2 * n + 1
s = input()
cnt = 0
check_s = "IO" * (check_length // 2) + "I"
# print("check_s", check_s)

for i in range(0, len(s) - check_length + 1):
    small_s = s[i : i + check_length]
    # print(small_s)
    if small_s == check_s:
        # print("plus enter")
        cnt += 1
print(cnt)