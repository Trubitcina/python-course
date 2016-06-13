import sqlite3 as sq


with sq.connect("data.sqlite") as con:
    cur = con.cursor()
    # 1
    for a in cur.execute(
        "select * "
        "from Users "
    ):
        print(a)

    # 2
    for b in cur.execute(
        "select count(*) "
        "from Users "
    ):
        print(b)

    # 3
    for c in cur.execute(
       "select count(*) "
       "from Users "
       "where birth_date <= date('1976-05-18') "
    ):
        print(c)

    # 4
    for d in cur.execute(
        "select country, count(*) "
        "from Users "
        "group by country "
    ):
        print(d)

    # 5
    for e in cur.execute(
        "select name "
        "from Users "
        "group by name "
        "having count(name) > 1 "
    ):
        print(e)

    # 6
    for f in cur.execute(
         "select count(*) "
         "from Orders "
         "where created >= date('2016-01-01') "
    ):
        print(f)

    # 7
    for g in cur.execute(
        "select date(created), count(*) as n from Orders "
        "group by date(created) "
        "order by n desc limit 1 "
    ):
        print(g)

    # 8
    for h in cur.execute(
        "select 100 - sum(paid) * 100.0 / count(*) from Orders"
    ):
        print(h)

    # 9
    for i in cur.execute(
        "select * "
        "from Goods "
        "where name like '%bread%'"
    ):
        print(i)

    # 10
    for j in cur.execute(
        "select id, name, count(*) as n "
        "from GoodsInOrders "
        "inner join Goods "
        "on id = good_id "
        "group by good_id "
        "order by n desc limit 10"
    ):
        print(j)

    # 11
    for k in cur.execute(
        "select sum(price) "
        "from Orders "
        "inner join GoodsInOrders "
        "on order_id = orders.id "
        "inner join Goods "
        "on Goods.id = GoodsInOrders.good_id "
        "where created like '2016%' and paid = 1 "
    ):
        print(k)
