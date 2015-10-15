__author__ = 'Нина'


def plural(n, thing):
    n %= 100
    n1 = n % 10
    if 10 < n < 20:
        return thing[2]
    elif 1 < n1 < 5:
        return thing[1]
    elif n1 == 1:
        return thing[0]
    else:
        return thing[2]

things = {'утюг': ['утюг', 'утюга', 'утюгов'],
         'ложка': ['ложка', 'ложки', 'ложек'],
         'гармошка': ['гармошка', 'гармошки', 'гармошек'],
         'чайник': ['чайник', 'чайника', 'чайников']}

thing = input()
count = int(input())

print(" ".join((str(count), plural(count, things[thing]))))
