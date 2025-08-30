# Vowel Counter Dictionary (Nested for loop edition)


S = 'power star'
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
    vowel_count = 0
    for c in w:
        if c.lower() in 'aeiou':
            vowel_count += 1
    Out[w] = vowel_count

print(f"Output: {Out}")