# Word Reverser Dictionary Builder using for loop


S = 'power star'
words = S.split()
reversed_dict = {}
for word in words:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    reversed_dict[word] = reversed_word

print(f"Output: {reversed_dict}")