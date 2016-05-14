import sqlite3 as sq


with sq.connect("data.sqlite") as con:  # открыли соединение с базой данных
    cur = con.cursor()
    for a in cur.execute(
        "select username "
        "from Users "):
        print(a)

    for b in cur.execute(
        "select username "
        "from Users "
        "order by registered asc "
        "limit 5 "
    ):
        print(b)

    for c in cur.execute(
        "select Users.username, count(*) as listened "
        "from Users "
        "inner join Listened "
        "on Users.id = Listened.user_id "
        "group by Users.id "
        "order by listened desc "
        "limit 5"

    ):
        print(c)

    for d in cur.execute(
        "select Artists.name, count(*) as album "
        "from Artists "
        "inner join Albums "
        "on Artists.id = Albums.artist_id "
        "group by Artists.id"

    ):
        print(d)

    for e in cur.execute(
        "select Artists.name, count(*) as songs "
        "from Artists, Albums, Songs "
        "where Artists.id = Albums.artist_id and Albums.id = Songs.album_id "
        "group by Artists.id"

    ):
        print(e)

    for f in cur.execute(
        "select Artists.name, Albums.name, count(*) as songs  "
        "from Artists, Albums, Songs "
        "where Albums.artist_id = Artists.id and Albums.id = Songs.album_id "
        "group by Artists.id "
        "order by songs desc limit 1"
    ):
        print(f)

    for f in cur.execute(
        "select Artists.name, Albums.name, total(duration)  "
        "from Artists, Albums, Songs "
        "where Albums.artist_id = Artists.id and Albums.id = Songs.album_id "
        "group by Albums.id "
        "order by total(duration) desc limit 1"
    ):
        print(f)