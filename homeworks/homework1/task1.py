a = input()
b = int(input())
if b == 0 or 5 <= b <= 20 or b % 10 == 0 or b % 10 == 5 or \
    b % 10 == 6 or b % 10 == 7 or b % 10 == 8 or b % 10 == 9 \
    or b % 100 == 11 or b % 100 == 12 or b % 100 == 13 or b % 100 == 14:
    if a == "утюг":
        print(b, a + 'ов')
    else:
        print(b, 'ложек')
elif b == 1 or b % 10 == 1:
    if a == "утюг":
        print(b, a)
    else:
        print(b, a)
elif 2 <= b <= 4 or b % 10 == 2 or b % 10 == 3 or b % 10 == 4:
    if a == "утюг":
        print(b, a + 'а')
    else:
        print(b, 'ложки')
