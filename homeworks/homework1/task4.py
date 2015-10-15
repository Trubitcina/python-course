import collections
str1 = input()
str = collections.Counter(str1)
list_str = list(str)
list_str.sort()
for i in list_str:
    print(i, str[i])
    
