def is_mirror(a):
    n=len(a)
    if n%2 !=0:
        print(False)
    else:
        mid=n//2
        st=a[:mid]
        fi=a[mid:]
        #print(st)
        #print(fi)
        if st==fi[::-1]:
            print(True)
        else:
            print(False)
arr = list(map(int, input("Enter the list (space-separated): ").split()))
is_mirror(arr)