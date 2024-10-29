word = input()
result = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        tmp_word = ""
        first_word = word[0 : i]
        second_word = word[i : j]
        third_word = word[j : ]
        tmp_word += first_word[::-1]
        tmp_word += second_word[::-1]
        tmp_word += third_word[::-1]
        result.append(tmp_word)
result = sorted(result)
print(result[0])
