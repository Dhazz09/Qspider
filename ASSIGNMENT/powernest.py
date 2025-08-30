# Word Length Dictionary Builder (No len(), nested for loop)

S = 'power star'
words = []
word = ""
for char in S:
    if char != ' ':
        word += char
    else:
        words.append(word)
        word = ""
words.append(word)  
Out = {}
for w in words:
    count = 0
    for ch in w:
        count += 1
    Out[w] = count

print(f"Output: {Out}")