#  Custom Word Mapper using for loop

In = 'push maadi kushi padi'
words = In.split()
Out = {}
for word in words:
    if word == 'push':
        Out[word] = word[-2:]  
    elif word == 'maadi' or word == 'kushi':
        mid_index = len(word) // 2
        Out[word] = word[mid_index]  
    elif word == 'padi':
        Out[word] = word[0] + word[-1]  
    else:
        Out[word] = "?" 

print(f"Output: {Out}")