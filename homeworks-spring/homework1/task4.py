n = int(input())
stack = input().split()
m = int(input())
funlist = []
for i in range(m):
    funlist.append(input())
ex = input()
funlib = {}

for i in funlist:
    if i.split()[0] in funlib:
        funlib[i.split()[0]][i.split()[1]] = i.split()[2]
    else:
        funlib[i.split()[0]] = {i.split()[1]: i.split()[2]}


for fun in reversed(stack):
    if ex in funlib[fun]:
        if funlib[fun][ex] != '_':
            ex = funlib[fun][ex]
            n -= 1
        else:
            break

    else:
        n -= 1

print(' '.join(stack[:n]))
