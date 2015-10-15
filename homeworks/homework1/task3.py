lst = list(map(int, input().split()))
lst1 = sorted(lst[1::2], reverse=True)
lst2 = sorted(lst[::2])
lst[1::2] = lst1
lst[::2] = lst2
for i in lst:
    print(i, end=' ')
    
