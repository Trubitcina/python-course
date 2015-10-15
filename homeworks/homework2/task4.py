__author__ = 'Нина'


def rpfilter(a, *args):
    lst_out = []

    def euclid(x, y):
        return x if y == 0 else euclid(y, x % y)

    for i in args:
        if euclid(a, i) == 1:
            lst_out.append(i)
    return lst_out
lst_in = (int(i) for i in input().split())
lst_out = rpfilter(*lst_in)
if lst_out != []:
    for i in lst_out:
        print(i, end=' ')
else:
    print(None)
