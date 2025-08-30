# Triple Logic Dictionary Builder (Nested for loop edition)

S = 'kabab is love'
words = []
word = ""
for ch in S:
    if ch != ' ':
        word += ch
    else:
        words.append(word)
        word = ""
words.append(word)  
Out = {}
for w in words:
    reversed_word = ""
    for i in range(len(w) - 1, -1, -1):
        reversed_word += w[i]
    vowel_count = 0
    for ch in w:
        if ch.lower() in 'aeiou':
            vowel_count += 1
    even_chars = ""
    index = 0
    for ch in w:
        if index % 2 == 0:
            even_chars += ch
        index += 1
    Out[w] = [reversed_word, vowel_count, even_chars]

print(f" Output: {Out}")