import re


class Song:  # 1 преобразование класса Song (classes.py)
    def __init__(self, artist, name, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration

    def __repr__(self):
        song = "Song \"" + self.name + "\" by " + self.artist + self.album + \
            self.position + self.year + self.duration
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def import_songs(file_name):
    with open(file_name, 'r') as songs:
        songslist = songs.read()
    songslist = songslist.split('\n')
    songs = []
    for song in songslist:
        name, artist, album, position, year, duration = song.split('\t')
        songs.append(Song(artist, name, album, position, year, duration))
    return(songs)

songs = import_songs('songs1.txt')


def export_songs(songs, file_name):
    out_file = open(file_name, 'w')
    for song in songs:
        out_file.write('%s\t' % song)
    out_file.close()


def shuffle_songs(songs):
    from random import shuffle
    shuffle(songs)
    return songs


# 2 самый частый исп.(по песням)
d = dict()
for song in songs:
    if song.artist not in d:
        d[song.artist] = 1
    else:
        d[song.artist] += 1
count = ['', 0]
for x in d:
    if d[x] > count[1]:
        count = [x, d[x]]
print(count[0])

# с. длинная песня
length = 0
for song in songs:
    if int(song.duration) > int(length):
        length = song.duration
        max_length = (song.name + '\t' + song.artist)
print(max_length)

# с. длинный альбом
d = dict()
for song in songs:
    x = song.album+'\t'+song.artist
    if x not in d:
        d[x] = int(song.duration)
    else:
        d[x] += int(song.duration)
inv = {}
for k, v in d.items():
    keys = inv.setdefault(v, [])
    keys.append(k)
for i in inv[max(inv.keys())]:
    print(i)

# 10 с. частых слов
words = {}
for song in songs:
    songwords = re.findall('[a-zA-Z]+', song.name)
    for word in songwords:
        word = word.lower()
        words[word] = words.get(word, 0) + 1
inv = {}
for k, v in words.items():
    keys = inv.setdefault(v, [])
    keys.append(k)
n = 0
wordlist = []
while n < 10:
    ww = inv[max(inv.keys())]
    for i in ww:
        wordlist.append(i)
    del(inv[max(inv.keys())])
    n += 1
print('\t'.join(wordlist))

# с. продуктивный исп.
d = dict()
albums = []
for song in songs:
    if song.artist not in d:
        d[song.artist] = 1
    else:
        if song.album in albums:
            continue
        else:
            d[song.artist] += 1
    albums.append(song.album)
inv = {}
for k, v in d.items():
    keys = inv.setdefault(v, [])
    keys.append(k)
most_artist = list(inv[max(d.values())])
print(most_artist[0])
