d = {}
l = []
n = int(input())
for i in range(n):
    classes = (input().split(" "))
    if len(classes) == 1:
        d[classes[0]] = []
    else:
        d[classes[0]] = classes[2:]


def parent(c1):
    if c1 in l:
        return
    l.append(c1)
    for c2 in d[c1]:
        if c2 not in l:
            parent(c2)


m = int(input())
for j in range(m):
    ans = input().split(" ")
    parent(ans[1])
    if ans[0] not in l:
        print('No')
    else:
        print('Yes')
    l = []
