a = list(map(int, input("Enter the list (space-separated): ").split()))
target = int(input("Enter the target: "))
out = []
for i in range(len(a)):
    if a[i] == target:
        out.append([a[i]])
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            out.append([a[i], a[j]])
print(out)
